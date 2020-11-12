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

#ifndef typedef_SFc3_sf_aircraft_faultInstanceStruct
#define typedef_SFc3_sf_aircraft_faultInstanceStruct

typedef struct {
  SimStruct *S;
  ChartInfoStruct chartInfo;
  uint32_T chartNumber;
  uint32_T instanceNumber;
  int32_T c3_sfEvent;
  uint8_T c3_tp_Actuators;
  uint8_T c3_tp_LO;
  uint8_T c3_tp_L1;
  uint8_T c3_tp_Passive;
  uint8_T c3_tp_Active;
  uint8_T c3_tp_Standby;
  uint8_T c3_tp_Off;
  uint8_T c3_tp_Isolated;
  uint8_T c3_tp_RO;
  uint8_T c3_b_tp_L1;
  uint8_T c3_b_tp_Passive;
  uint8_T c3_b_tp_Active;
  uint8_T c3_b_tp_Standby;
  uint8_T c3_b_tp_Off;
  uint8_T c3_b_tp_Isolated;
  uint8_T c3_tp_LI;
  uint8_T c3_c_tp_L1;
  uint8_T c3_c_tp_Passive;
  uint8_T c3_c_tp_Active;
  uint8_T c3_c_tp_Standby;
  uint8_T c3_c_tp_Off;
  uint8_T c3_c_tp_Isolated;
  uint8_T c3_tp_RI;
  uint8_T c3_d_tp_L1;
  uint8_T c3_d_tp_Passive;
  uint8_T c3_d_tp_Active;
  uint8_T c3_d_tp_Standby;
  uint8_T c3_d_tp_Off;
  uint8_T c3_d_tp_Isolated;
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
  int32_T c3_fails;
  int32_T c3_b_fails;
  int32_T c3_c_fails;
  int32_T c3_d_fails;
  uint8_T c3_doSetSimStateSideEffects;
  const mxArray *c3_setSimStateSideEffectsInfo;
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
extern struct SfDebugInstanceStruct *sfGlobalDebugInstanceStruct;

/* Variable Definitions */

/* Function Declarations */
extern const mxArray *sf_c3_sf_aircraft_fault_get_eml_resolved_functions_info
  (void);

/* Function Definitions */
extern void sf_c3_sf_aircraft_fault_get_check_sum(mxArray *plhs[]);
extern void c3_sf_aircraft_fault_method_dispatcher(SimStruct *S, int_T method,
  void *data);

#endif
