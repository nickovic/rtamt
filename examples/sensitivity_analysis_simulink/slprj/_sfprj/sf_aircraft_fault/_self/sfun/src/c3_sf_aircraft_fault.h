#ifndef __c3_sf_aircraft_fault_h__
#define __c3_sf_aircraft_fault_h__

/* Type Definitions */
#ifndef struct_PositionBus_tag
#define struct_PositionBus_tag

struct PositionBus_tag
{
  real_T L_pos[2];
  boolean_T L_pos_fail[2];
  real_T R_pos[2];
  boolean_T R_pos_fail[2];
  real_T H1_press;
  real_T H2_press;
  real_T H3_press;
  boolean_T low_press[3];
};

#endif                                 /*struct_PositionBus_tag*/

#ifndef typedef_c3_PositionBus
#define typedef_c3_PositionBus

typedef struct PositionBus_tag c3_PositionBus;

#endif                                 /*typedef_c3_PositionBus*/

#include "sf_aircraft_ModeType.h"
#ifndef typedef_SFc3_sf_aircraft_faultInstanceStruct
#define typedef_SFc3_sf_aircraft_faultInstanceStruct

typedef struct {
  SimStruct *S;
  ChartInfoStruct chartInfo;
  int32_T c3_sfEvent;
  uint8_T c3_is_active_c3_sf_aircraft_fault;
  uint8_T c3_is_c3_sf_aircraft_fault;
  uint8_T c3_is_LO;
  uint8_T c3_is_active_LO;
  uint8_T c3_is_RO;
  uint8_T c3_is_active_RO;
  uint8_T c3_is_LI;
  uint8_T c3_is_active_LI;
  uint8_T c3_is_RI;
  uint8_T c3_is_active_RI;
  uint8_T c3_JITStateAnimation[29];
  int32_T c3_fails;
  int32_T c3_b_fails;
  int32_T c3_c_fails;
  int32_T c3_d_fails;
  uint8_T c3_JITTransitionAnimation[104];
  void *c3_RuntimeVar;
  uint8_T c3_doSetSimStateSideEffects;
  const mxArray *c3_setSimStateSideEffectsInfo;
  uint32_T c3_mlFcnLineNumber;
  void *c3_fcnDataPtrs[4];
  char_T *c3_dataNames[4];
  uint32_T c3_numFcnVars;
  uint32_T c3_ssIds[4];
  uint32_T c3_statuses[4];
  void *c3_outMexFcns[4];
  void *c3_inMexFcns[4];
  CovrtStateflowInstance *c3_covrtInstance;
  void *c3_fEmlrtCtx;
  sf_aircraft_ModeType *c3_LO_mode;
  sf_aircraft_ModeType *c3_RO_mode;
  sf_aircraft_ModeType *c3_LI_mode;
  sf_aircraft_ModeType *c3_RI_mode;
  c3_PositionBus *c3_u;
} SFc3_sf_aircraft_faultInstanceStruct;

#endif                                 /*typedef_SFc3_sf_aircraft_faultInstanceStruct*/

/* Named Constants */

/* Variable Declarations */

/* Variable Definitions */

/* Function Declarations */
extern const mxArray *sf_c3_sf_aircraft_fault_get_eml_resolved_functions_info
  (void);

/* Function Definitions */
extern void sf_c3_sf_aircraft_fault_get_check_sum(mxArray *plhs[]);
extern void c3_sf_aircraft_fault_method_dispatcher(SimStruct *S, int_T method,
  void *data);

#endif
