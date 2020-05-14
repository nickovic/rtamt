import numpy as np
from webotPyLib import *

def plotBaseMap(plt, worldInfo):
    # plot obstacles
    obstacle1translation = worldInfo["obstacle1translation"]
    obstacle1size = worldInfo["obstacle1size"]
    polyRect1 = posSizeRect2poly((obstacle1translation[0], obstacle1translation[2]), (obstacle1size[0], obstacle1size[2]))
    plotPoly(plt, polyRect1, 'black')
    plt.text(obstacle1translation[2], obstacle1translation[0], r'$Obstacle_1$')
    obstacle2translation = worldInfo["obstacle2translation"]
    obstacle2size = worldInfo["obstacle2size"]
    polyRect2 = posSizeRect2poly((obstacle2translation[0], obstacle2translation[2]), (obstacle2size[0], obstacle2size[2]))
    plotPoly(plt, polyRect2, 'black')
    plt.text(obstacle2translation[2], obstacle2translation[0], r'$Obstacle_2$')
    
    # plot prohibit area
    prohibitArea1 = worldInfo["prohibitArea1"]
    plotPoly(plt, prohibitArea1, color='hotpink', linestyle='dashed')
    plt.text(-0.5, 0.4, r'$ProhibitedArea_1$', color='hotpink')
    prohibitArea2 = worldInfo["prohibitArea2"]
    plotPoly(plt, prohibitArea2, color='hotpink', linestyle='dashed')
    plt.text(0.85, -0.9, r'$ProhibitedArea_2$', color='hotpink')

    # plot
    plt.gca().set_aspect('equal', adjustable='box')
    floorTranslation = worldInfo["floorTranslation"]
    floorSize = worldInfo["floorSize"]
    plt.xlim(floorTranslation[1]+floorSize[1]/2, floorTranslation[1]-floorSize[1]/2)
    plt.xlabel('Y [m]')
    plt.ylim(floorTranslation[0]-floorSize[0]/2, floorTranslation[0]+floorSize[0]/2)
    plt.ylabel('X [m]')
    
    return plt


def plotMapAgents(plt, data):
    ag1x = np.asarray([i[1] for i in data["tagent1odox"]])
    ag1y = np.asarray([i[1] for i in data["tagent1odoy"]])
    plt.plot(ag1y, ag1x, linestyle='dashed', color='orange', label='Agent1')
    ag2x = np.asarray([i[1] for i in data["tagent2odox"]])
    ag2y = np.asarray([i[1] for i in data["tagent2odoy"]])
    plt.plot(ag2y, ag2x, linestyle='dotted', color='orange', label='Agent2')
    return plt
    

def plotWaypoint(plt, worldInfo):
    wayPoints = worldInfo["wayPoints"]
    x,y = wayPoints.xy
    plt.plot(y, x, marker='o', color='limegreen', label='Waypoints')


def plotmap(plt, worldInfo, data):
    # plot base world
    plotBaseMap(plt, worldInfo)
    
    # plot target path
    plotWaypoint(plt, worldInfo)

    # plot agent
    plotMapAgents(plt, data)
    
    # plot ego odometory
    # plt.gca().set_title('odometory')
    egox = np.asarray([i[1] for i in data["tegoodox"]])
    egoy = np.asarray([i[1] for i in data["tegoodoy"]])
    plt.plot(egoy, egox, color='deepskyblue', label='Ego path')

    return plt


def plotPoly(plt, poly, color='black', linestyle='solid'):
    ext=list(poly.exterior.coords)
    x = np.asarray([i[0] for i in ext])
    y = np.asarray([i[1] for i in ext])
    plt.plot(y, x, linestyle=linestyle, color=color)
    
    return plt


def dicTraj2tx(dic, name):
    time = np.asarray([i[0] for i in dic[name]])
    x = np.asarray([i[1] for i in dic[name]])
    return time, x


def plotDicTrajWithSTLresult(plt, dic, name, req):
    time,x = dicTraj2tx(dic, name)
    if req >= 0:
        plt.plot(time, x, linestyle='solid', color='blue', label='True')
    else:
        plt.plot(time, x, linestyle='dashdot', color='red', label='False')
    plt.xlabel('Time [sec]')
