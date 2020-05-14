import struct
import math
import numpy
from numpy.linalg import norm
from shapely.geometry import Polygon, Point, LinearRing, LineString
from shapely import affinity

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from webotPlotLib import *

class xythCoord:
    x = []
    y = []
    th = []
    time = []
    
    
    def __init__(self, x, y, th, time):
        self.x = x
        self.y = y
        self.th = th
        self.time = time
    
    
    def __sub__(self, other):
        subX = self.x - other.x
        subY = self.y - other.y
        subTh = self.th - other.th
        subTime = self.time - other.time
        return xythCoord(subX, subY, subTh, subTime)


    def __add__(self, other):
        subX = self.x + other.x
        subY = self.y + other.y
        subTh = self.th + other.th
        subTime = self.time + other.time
        return xythCoord(subX, subY, subTh, subTime)
        

def getRobotSampleXYTh(robot):
    translationValues = robot.getField('translation').getSFVec3f()
    rotationValues = robot.getField('rotation').getSFRotation()
    #!!---change coordination also.--!!
    th = rotationValues[3]+(math.pi/2)
    if th > math.pi:
        sth = -2*math.pi+th
    else:
        sth = th
    
    xyth = (translationValues[0], -translationValues[2], sth)
    return xyth
    
    
def posSizeRect2poly(rectPos, rectSize):
    rectSizeH = numpy.array(rectSize)/2.0
    polyRect = Polygon([(rectPos[0]+rectSizeH[0], rectPos[1]+rectSizeH[1]),
                        (rectPos[0]-rectSizeH[0], rectPos[1]+rectSizeH[1]),
                        (rectPos[0]-rectSizeH[0], rectPos[1]-rectSizeH[1]),
                        (rectPos[0]+rectSizeH[0], rectPos[1]-rectSizeH[1])])
    return polyRect


def distP2P(p1x, p1y, p2x, p2y):
    point1 = Point((p1x, p1y))
    point2 = Point((p2x, p2y))
    dist = point1.distance(point2)
    return dist


def distTraj2Traj(trajX1, trajY1, trajX2, trajY2):
    distTraj = []
    for ix1, iy1, ix2, iy2 in zip(trajX1, trajY1, trajX2, trajY2):
        dist = distP2P(ix1[1], iy1[1], ix2[1], iy2[1])
        distTraj.append( (ix1[0], dist) )
    return distTraj


def distP2Po(poly, point):
    #defining sigined distance
    dist = poly.exterior.distance(point)
    if (point.within(poly)):
        dist = -dist
    return dist


def distP2R(rectPos, rectSize, pointPos):
    #TODO consider rotation
    #Pos and Size are 2D
    polyRect = posSizeRect2poly(rectPos, rectSize)
    point = Point(pointPos[0], pointPos[1])
    dist = distP2Po(polyRect, point)
    return dist


def distTraj2Po(poly, trajX, trajY):
    distTraj = []
    for ix, iy in zip(trajX, trajY):
        point = Point(ix[1], iy[1])
        dist = distP2Po(poly, point)
        distTraj.append( (ix[0], dist) )
    return distTraj


def distTraj2R(rectPos, rectSize, trajX, trajY):
    polyRect = posSizeRect2poly(rectPos, rectSize)
    distTraj = distTraj2Po(polyRect, trajX, trajY)
    return distTraj


# implimenting!
def distLineStr2Po(poly, line):
    #defining sigined distance
    dist = poly.exterior.distance(line)
#    if(line.crosses(poly)):
#        dist = poly.exterior.distance(line.interpolate(0.0001))
    return dist
    
def distLineStr2R(rectPos, rectSize, line):
    polyRect = posSizeRect2poly(rectPos, rectSize)
    dist = polyRect.exterior.distance(line)
    return dist


def getLatestPacket(receiver):
    packet = []
    #print(receiver.getQueueLength())
    while receiver.getQueueLength():
        if receiver.getQueueLength() == 1:
            packet = receiver.getData()
        receiver.nextPacket()
        
    return packet


def getLatestPositionXyth(receiver):
    packet = getLatestPacket(receiver)
    xyth = []
    if packet != []:            
        xyth = struct.unpack('fff', packet)
    else:
        print('no data!')

    return xyth


def getLatestEgoInternalParam(receiver):
    cV = 0.0
    cW = 0.0
    oV = 0.0
    oW = 0.0
    state = xythCoord(0.0, 0.0, 0.0, 0.0)
    ag1state = xythCoord(0.0, 0.0, 0.0, 0.0)
    ag2state = xythCoord(0.0, 0.0, 0.0, 0.0)
    
    packet = getLatestPacket(receiver)
    if packet != []:            
        data = struct.unpack('fffffffffff', packet)
        cV = data[0]
        cW = data[1]
        oV = data[2]
        oW = data[3]
        state.x = data[4]
        state.y = data[5]
        state.th = data[6]
        ag1state.x = data[7]
        ag1state.y = data[8]
        ag2state.x = data[9]
        ag2state.y = data[10]
        
    else:
        print('no data!')

    return cV, cW, oV, oW, state, ag1state, ag2state


def closetLineOfWaypoits(tPoint, wayPoints):
    
    lines = []
    dists = []
    for i in range(1, len(wayPoints.coords)):
        sPoint = list(wayPoints.coords)[i-1]
        ePoint = list(wayPoints.coords)[i]
        line = LineString([sPoint, ePoint])
        #print(list(line.coords))
        lines.append(line)
        
        dist = line.distance(tPoint)
        #print(str(dist))
        dists.append(dist)
    
    mi = numpy.argmin(numpy.array(dists))
    cDist = dists[mi]
    cLine = lines[mi]
    #print(mi)
    #print(str(list(cLine.coords)) + ' ' + str(cDist))

    return cLine, cDist


def signedDistansL2P(line, point):
    sPoint = numpy.array(list(line.coords)[0])
    ePoint = numpy.array(list(line.coords)[1])
    oPoint = numpy.array(point.coords)
    sDist = numpy.cross(sPoint-ePoint, sPoint-oPoint)/norm(sPoint-ePoint)

    return sDist[0]
    

def radLine(line):
    
    sPoint = numpy.array(list(line.coords)[0])
    ePoint = numpy.array(list(line.coords)[1])
    vec = ePoint - sPoint
    rad = math.atan2(vec[1], vec[0])
    
    return rad

class vPcontroller:
    
    def __init__(self, Kv):
        self.Kv = Kv
    
    def calcReferenceV(self, currentV, targetV, deltaT):
        diffV = currentV - targetV
        Vref = -self.Kv*(diffV)
        nextV = currentV + Vref*deltaT
        #print('diffV=' + str(diffV) + '[m/s] cV=' + str(cV) + '[m/s] targetV=' + str(targetV) + '[m/s] deltaT=' + str(deltaT) + '[s]') 
        #print('+Vref*deltaT='+str(Vref*deltaT))
        
        return nextV
        

class wayPointsTraceController:
    
    def __init__(self, Kd, Kth, Kw, Kv):
        self.Kd = Kd
        self.Kth = Kth
        self.Kw = Kw
        self.Kv = Kv
        self.vCon = vPcontroller(self.Kv)
        
    def calcReferenceW(self, cX, cY, cTh, cW, wayPoints, targetV, deltaT):
    
        oLine, dist = closetLineOfWaypoits(Point(cX, cY), wayPoints)
        sDist = signedDistansL2P(oLine, Point(cX, cY))
        lRad = radLine(oLine)
        dRad = cTh - lRad 
        #print('lRad=' + str(lRad) + '[rad] cTh=' + str(cTh) + '[rad]')
        #print('sDist=' + str(sDist) + '[m] dRad=' + str(dRad) + '[rad] Omega=' + str(cW) + '[rad/s] deltaT=' + str(deltaT) + '[s]') 
    
        Wref = -self.Kd*sDist -self.Kth*dRad -self.Kw*cW
        nextW = cW + Wref*deltaT
        #print('+Wref*deltaT='+str(Wref*deltaT))
    
        return nextW

    def calcReferenceVW(self, cX, cY, cTh, cV, cW, wayPoints, targetV, deltaT):

        # rW
        rW = self.calcReferenceW(cX, cY, cTh, cW, wayPoints, targetV, deltaT)
        # rV
        rV = self.vCon.calcReferenceV(cV, targetV, deltaT)
    
        return rV, rW


def trajGen(v, w, time, dt):
    geom = Point(0.0, 0.0)
    traj = []
    for step in numpy.arange(0, time, dt):
        matrix = [math.cos(w*dt), -math.sin(w*dt), math.sin(w*dt), math.cos(w*dt), v*dt, 0]
        geom = affinity.affine_transform(geom, matrix)
        #print(geom)
        traj.append(geom)
    return LineString(traj)


def trajCollisonCheck(traj, vitualObjects):
    dists = []
    for object in vitualObjects:
        dist = traj.distance(object)
        dists.append(dist)
     
    minDist = numpy.array(dists).min()    
    return minDist


class DWAcontroller:

    def __init__(self, maxV, dV, maxA, maxW, dW, maxAW, dt, estimateTime):
        self.maxV = maxV
        self.dV = dV
        self.maxA = maxA
        self.maxW = maxW
        self.dW = dW
        self.maxAW = maxAW
        self.dt = dt
        self.estimateTime = estimateTime
                

    def genVW(self):
        self.ws = numpy.arange(-self.maxW, +self.maxW+self.dW, self.dW)
        self.vs = numpy.arange(0, +self.maxV+self.dV, self.dV)
        return self.vs, self.ws
        
        
    def genFilteredVW(self, targetV, targetW):
        self.ws = self.ws[numpy.logical_and(targetW-self.maxAW<=self.ws, self.ws<=targetW+self.maxAW)]
        self.vs = self.vs[numpy.logical_and(targetV-self.maxA <=self.vs, self.vs<=targetV+self.maxA)]
        return self.vs, self.ws


    def genTrjCandidates(self):
        self.trajs = []
        for w in self.ws:
            vTrajMap = []
            for v in self.vs:
                traj = trajGen(v, w, self.estimateTime, self.dt)
                vTrajMap.append(traj)
            self.trajs.append(vTrajMap)


    def vwTrajMapCollisonCheck(self, vitualObjects, dim):
        self.dists = numpy.zeros([self.ws.size, self.vs.size])
        for wi, wTrajs in enumerate(self.trajs):
            for vi, traj in enumerate(wTrajs):
                dist = trajCollisonCheck(traj, vitualObjects)
                dist -= dim                         
                self.dists[wi][vi] = dist
    
    
    def calcReferenceVW(self, targetV, targetW, obstacles, dim):
        #TODO: Is gain parametr is here good?  
        Kh = 0.2
        kd = 1.0
        Kv = Kh*10


        # 1. genVW list
        self.genVW()
        self.genFilteredVW(targetV, targetW) #Dynamic Window

        # 2. vw map generate
        self.genTrjCandidates()
        
        # 3. objective
        self.vwTrajMapCollisonCheck(obstacles, dim)
        
        # cost evaluation
        self.Gs = numpy.zeros([self.ws.size, self.vs.size])
        self.gHeads = numpy.zeros([self.ws.size, self.vs.size])
        self.gDists = numpy.zeros([self.ws.size, self.vs.size])
        self.gVels = numpy.zeros([self.ws.size, self.vs.size])

        for wi in range(self.ws.size):	#TODO: array can be use. not use for loop
            for vi in range(self.vs.size):
                w = self.ws[wi]
                v = self.vs[vi]
                dist = self.dists[wi][vi]
                heading = numpy.pi/12 - numpy.abs(targetW-w)
                velocity = self.maxV - numpy.abs(targetV-v)
                self.gHeads[wi][vi] = Kh*heading
                self.gDists[wi][vi] = kd*dist
                self.gVels[wi][vi] = Kv*velocity
                #print('G=' +  str(G) + ' heading=' +  str(heading) + ' dist=' + str(dist) + ' velocity=' + str(velocity))
    		    
        self.Gs = self.gHeads + self.gDists + self.gVels

        maxIndex = numpy.unravel_index(self.Gs.argmax(), self.Gs.shape)
        #print(maxIndex)
        #print(self.Gs[maxIndex] == self.Gs.max())  
        self.oV = self.vs[maxIndex[1]]
        self.oW = self.ws[maxIndex[0]]
        
        # choose target vw
        originTraj = trajGen(targetV, targetW, self.estimateTime, self.dt)
        originDist = trajCollisonCheck(originTraj, obstacles)
        originDist -= dim
        if originDist > dim:
            self.oV = targetV
            self.oW = targetW
            
        print('DWA oV=' + str(self.oV) + ' oW=' + str(self.oW) )
    
        return self.oV, self.oW


    def plotGainMap(self, axGain, axGainVW, axGainDist):

        axGain.cla()
        X, Y = numpy.meshgrid(self.ws, self.vs)
        Z = self.Gs.T
        axGain.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        axGain.set_xlim([self.maxW, -self.maxW])
        axGain.set_ylim([0.0, self.maxV])
        axGain.set_xlabel('w')
        axGain.set_ylabel('v')
        axGain.set_title('Gs')

        axGainVW.cla()
        X, Y = numpy.meshgrid(self.ws, self.vs)
        Z = (self.gHeads+self.gVels).T
        axGainVW.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        axGainVW.set_xlim([self.maxW, -self.maxW])
        axGainVW.set_ylim([0.0, self.maxV])
        axGainVW.set_xlabel('w')
        axGainVW.set_ylabel('v')
        axGainVW.set_title('gHead+gVels');
        
        axGainDist.cla()
        X, Y = numpy.meshgrid(self.ws, self.vs)
        Z = self.gDists.T
        axGainDist.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        axGainDist.set_xlim([self.maxW, -self.maxW])
        axGainDist.set_ylim([0.0, self.maxV])
        axGainDist.set_xlabel('w')
        axGainDist.set_ylabel('v')
        axGainDist.set_title('gDists');
    
    
    def plotResult(self, ax, targetV, targetW, vitualObstacles, dim):
        ax.cla()
        ax.set_aspect('equal', adjustable='box')
        xmax = self.maxV*self.estimateTime*0.8
        ymax = self.maxV*self.estimateTime*1.2
        ax.set_xlim([xmax,-xmax])
        ax.set_ylim([-ymax*0.1, ymax])
        plt.xlabel('Y [m]')
        plt.ylabel('X [m]')
        
        # plot Ego
        egoShape = Polygon([(  0.07,  0.00),
                            (  0.04,  0.04),
                            ( -0.04,  0.04),
                            ( -0.04, -0.04),
                            (  0.04, -0.04)])
        plotPoly(ax, egoShape, color='deepskyblue', linestyle='solid')
        
        # plot target VW 
        targetTraj = trajGen(targetV, targetW, self.estimateTime, self.dt)
        x, y = targetTraj.xy
        pathFollow_handle, = ax.plot(y, x, linestyle='dashed', color='orange', zorder=3, linewidth=2.0, label='Path Follower order')
        
        # plot vmTrajMap
        for wi in range(self.ws.size):
            for vi in range(self.vs.size):
                x,y = self.trajs[wi][vi].xy
                if self.dists[wi][vi] >= 0:
                    candidate_handle, = ax.plot(y, x, linestyle='dotted', linewidth=1.0, color='gray', zorder=1, label='DWA candidates')
                else:
                    #ax.plot(y, x, color='hotpink', zorder=0)
                    pass 
                    
        # plot obstacle
        for circle in vitualObstacles:
            c = plt.Circle((circle.y, circle.x), dim/2.0, linewidth = 3.0, fc='white', ec='orange', zorder=1, label='Agent')
            ax.add_artist(c)    #TODO this c instance leads warrning.

        # plot solvedVW 
        targetTraj = trajGen(self.oV, self.oW, self.estimateTime, self.dt)
        x, y = targetTraj.xy
        final_handle, = ax.plot(y, x, color='red', zorder=3, linewidth=5.0, label='Decided order')

        plt.legend(handles=[final_handle, pathFollow_handle, candidate_handle])

     
def convertG2Rcoordination(RobotGstate, objectiveGpos):
    matrix = numpy.array([[math.cos(RobotGstate.th), -math.sin(RobotGstate.th), RobotGstate.x ],
                          [math.sin(RobotGstate.th),  math.cos(RobotGstate.th), RobotGstate.y ],
                          [0,                         0,                        1             ]])
    matrixInv = numpy.linalg.inv(matrix)
    #print(matrixInv)
    affineMatrix = [matrixInv[0][0], matrixInv[0][1], matrixInv[1][0], matrixInv[1][1], matrixInv[0][2], matrixInv[1][2]]
    objectiveRpos = affinity.affine_transform(objectiveGpos, affineMatrix)
    #print(objectiveRpos)
    return objectiveRpos

# plot
