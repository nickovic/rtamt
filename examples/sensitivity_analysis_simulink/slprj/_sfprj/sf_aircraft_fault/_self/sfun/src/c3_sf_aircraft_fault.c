/* Include files */

#include "sf_aircraft_fault_sfun.h"
#include "c3_sf_aircraft_fault.h"
#define CHARTINSTANCE_CHARTNUMBER      (chartInstance->chartNumber)
#define CHARTINSTANCE_INSTANCENUMBER   (chartInstance->instanceNumber)
#include "sf_aircraft_fault_sfun_debug_macros.h"
#define _SF_MEX_LISTEN_FOR_CTRL_C(S)   sf_mex_listen_for_ctrl_c(S);

static void chart_debug_initialization(SimStruct *S, unsigned int
  fullDebuggerInitialization);
static void chart_debug_initialize_data_addresses(SimStruct *S);
static const mxArray* sf_opaque_get_hover_data_for_msg(void *chartInstance,
  int32_T msgSSID);

/* Type Definitions */

/* Named Constants */
#define c3_event_go_isolated           (1)
#define c3_event_go_off                (2)
#define c3_event_E                     (0)
#define CALL_EVENT                     (-1)
#define c3_IN_NO_ACTIVE_CHILD          ((uint8_T)0U)
#define c3_IN_Actuators                ((uint8_T)1U)
#define c3_IN_Isolated                 ((uint8_T)1U)
#define c3_IN_L1                       ((uint8_T)2U)

/* Variable Declarations */

/* Variable Definitions */
static real_T _sfTime_;
static const char * c3_sv0[5] = { "Isolated", "Off", "Passive", "Standby",
  "Active" };

static const int32_T c3_iv0[5] = { 0, 1, 2, 3, 4 };

/* Function Declarations */
static void initialize_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void initialize_params_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void enable_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void disable_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_update_debugger_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static const mxArray *get_sim_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void set_sim_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray *c3_st);
static void c3_set_sim_state_side_effects_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void finalize_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void sf_gateway_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void mdl_start_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct *
  chartInstance);
static void c3_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void initSimStructsc3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_LO(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_RO(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_b_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_b_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_LI(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_c_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_c_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_enter_atomic_Active(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_RI(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_d_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_d_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_b_enter_atomic_Active(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_Off(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void init_script_number_translation(uint32_T c3_machineNumber, uint32_T
  c3_chartNumber, uint32_T c3_instanceNumber);
static void c3_L_switch(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_R_switch(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static real_T c3_LO_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static real_T c3_LI_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static real_T c3_RO_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static real_T c3_RI_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static const mxArray *c3_sf_marshallOut(void *chartInstanceVoid, void *c3_inData);
static int32_T c3_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_sfEvent, const char_T *c3_identifier);
static int32_T c3_b_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static void c3_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData);
static const mxArray *c3_b_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData);
static uint8_T c3_c_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_tp_Actuators, const char_T *c3_identifier);
static uint8_T c3_d_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static void c3_b_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData);
static const mxArray *c3_c_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData);
static sf_aircraft_ModeType c3_e_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray
   *c3_b_LO_mode, const char_T *c3_identifier);
static sf_aircraft_ModeType c3_f_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray *c3_b_u,
   const emlrtMsgIdentifier *c3_parentId);
static void c3_c_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData);
static const mxArray *c3_u_bus_io(void *chartInstanceVoid, void *c3_pData);
static const mxArray *c3_d_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData);
static const mxArray *c3_e_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData);
static boolean_T c3_g_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static void c3_d_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData);
static const mxArray *c3_f_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData);
static real_T c3_h_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static void c3_e_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData);
static const mxArray *c3_i_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_setSimStateSideEffectsInfo, const char_T
  *c3_identifier);
static const mxArray *c3_j_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static const mxArray *sf_get_hover_data_for_msg
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, int32_T c3_ssid);
static void c3_init_sf_message_store_memory(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static int32_T c3__s32_add__(SFc3_sf_aircraft_faultInstanceStruct *chartInstance,
  int32_T c3_b, int32_T c3_c, uint32_T c3_ssid_src_loc, int32_T
  c3_offset_src_loc, int32_T c3_length_src_loc);
static void init_dsm_address_info(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void init_simulink_io_address(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);

/* Function Definitions */
static void initialize_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  if (sf_is_first_init_cond(chartInstance->S)) {
    initSimStructsc3_sf_aircraft_fault(chartInstance);
    chart_debug_initialize_data_addresses(chartInstance->S);
  }

  chartInstance->c3_sfEvent = CALL_EVENT;
  _sfTime_ = sf_get_time(chartInstance->S);
  chartInstance->c3_doSetSimStateSideEffects = 0U;
  chartInstance->c3_setSimStateSideEffectsInfo = NULL;
  chartInstance->c3_tp_Actuators = 0U;
  chartInstance->c3_is_active_LI = 0U;
  chartInstance->c3_is_LI = c3_IN_NO_ACTIVE_CHILD;
  chartInstance->c3_tp_LI = 0U;
  chartInstance->c3_c_tp_Isolated = 0U;
  *chartInstance->c3_LI_mode = Isolated;
  chartInstance->c3_c_tp_L1 = 0U;
  chartInstance->c3_c_tp_Active = 0U;
  chartInstance->c3_c_tp_Off = 0U;
  chartInstance->c3_c_tp_Passive = 0U;
  chartInstance->c3_c_tp_Standby = 0U;
  chartInstance->c3_is_active_LO = 0U;
  chartInstance->c3_is_LO = c3_IN_NO_ACTIVE_CHILD;
  chartInstance->c3_tp_LO = 0U;
  chartInstance->c3_tp_Isolated = 0U;
  *chartInstance->c3_LO_mode = Isolated;
  chartInstance->c3_tp_L1 = 0U;
  chartInstance->c3_tp_Active = 0U;
  chartInstance->c3_tp_Off = 0U;
  chartInstance->c3_tp_Passive = 0U;
  chartInstance->c3_tp_Standby = 0U;
  chartInstance->c3_is_active_RI = 0U;
  chartInstance->c3_is_RI = c3_IN_NO_ACTIVE_CHILD;
  chartInstance->c3_tp_RI = 0U;
  chartInstance->c3_d_tp_Isolated = 0U;
  *chartInstance->c3_RI_mode = Isolated;
  chartInstance->c3_d_tp_L1 = 0U;
  chartInstance->c3_d_tp_Active = 0U;
  chartInstance->c3_d_tp_Off = 0U;
  chartInstance->c3_d_tp_Passive = 0U;
  chartInstance->c3_d_tp_Standby = 0U;
  chartInstance->c3_is_active_RO = 0U;
  chartInstance->c3_is_RO = c3_IN_NO_ACTIVE_CHILD;
  chartInstance->c3_tp_RO = 0U;
  chartInstance->c3_b_tp_Isolated = 0U;
  *chartInstance->c3_RO_mode = Isolated;
  chartInstance->c3_b_tp_L1 = 0U;
  chartInstance->c3_b_tp_Active = 0U;
  chartInstance->c3_b_tp_Off = 0U;
  chartInstance->c3_b_tp_Passive = 0U;
  chartInstance->c3_b_tp_Standby = 0U;
  chartInstance->c3_is_active_c3_sf_aircraft_fault = 0U;
  chartInstance->c3_is_c3_sf_aircraft_fault = c3_IN_NO_ACTIVE_CHILD;
  chartInstance->c3_fails = 0;
  _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_fails, 0U);
  chartInstance->c3_b_fails = 0;
  _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_b_fails, 1U);
  chartInstance->c3_c_fails = 0;
  _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_c_fails, 2U);
  chartInstance->c3_d_fails = 0;
  _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_d_fails, 3U);
  if (!(sf_get_output_port_reusable(chartInstance->S, 1) != 0)) {
    *chartInstance->c3_LO_mode = Isolated;
  }

  if (!(sf_get_output_port_reusable(chartInstance->S, 2) != 0)) {
    *chartInstance->c3_RO_mode = Isolated;
  }

  if (!(sf_get_output_port_reusable(chartInstance->S, 3) != 0)) {
    *chartInstance->c3_LI_mode = Isolated;
  }

  if (!(sf_get_output_port_reusable(chartInstance->S, 4) != 0)) {
    *chartInstance->c3_RI_mode = Isolated;
  }
}

static void initialize_params_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void enable_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  _sfTime_ = sf_get_time(chartInstance->S);
}

static void disable_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  _sfTime_ = sf_get_time(chartInstance->S);
}

static void c3_update_debugger_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  uint32_T c3_prevAniVal;
  c3_prevAniVal = _SFD_GET_ANIMATION();
  _SFD_SET_ANIMATION(0U);
  _SFD_SET_HONOR_BREAKPOINTS(0U);
  if (chartInstance->c3_is_active_c3_sf_aircraft_fault == 1U) {
    _SFD_CC_CALL(CHART_ACTIVE_TAG, 0U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_c3_sf_aircraft_fault == c3_IN_Actuators) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 0U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 0U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_active_LO == 1U) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 8U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 8U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_LO == c3_IN_L1) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 10U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 10U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LO_mode == Passive) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LO_mode == Active) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LO_mode == Standby) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 14U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 14U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LO_mode == Off) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 12U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 12U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_LO == c3_IN_Isolated) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_active_RO == 1U) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 22U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 22U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_RO == c3_IN_L1) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 24U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 24U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RO_mode == Passive) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RO_mode == Active) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RO_mode == Standby) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 28U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 28U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RO_mode == Off) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 26U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 26U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_RO == c3_IN_Isolated) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 23U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 23U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_active_LI == 1U) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 1U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 1U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_LI == c3_IN_L1) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LI_mode == Passive) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LI_mode == Active) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LI_mode == Standby) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 7U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 7U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_LI_mode == Off) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 5U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 5U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_LI == c3_IN_Isolated) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 2U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 2U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_active_RI == 1U) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 15U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 15U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_RI == c3_IN_L1) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 17U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 17U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RI_mode == Passive) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RI_mode == Active) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RI_mode == Standby) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 21U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 21U, chartInstance->c3_sfEvent);
  }

  if (*chartInstance->c3_RI_mode == Off) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 19U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 19U, chartInstance->c3_sfEvent);
  }

  if (chartInstance->c3_is_RI == c3_IN_Isolated) {
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 16U, chartInstance->c3_sfEvent);
  } else {
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 16U, chartInstance->c3_sfEvent);
  }

  _SFD_SET_ANIMATION(c3_prevAniVal);
  _SFD_SET_HONOR_BREAKPOINTS(1U);
  _SFD_ANIMATE();
}

static const mxArray *get_sim_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  const mxArray *c3_st;
  const mxArray *c3_y = NULL;
  sf_aircraft_ModeType c3_hoistedGlobal;
  const mxArray *c3_b_y = NULL;
  int32_T c3_b_u;
  const mxArray *c3_c_y = NULL;
  const mxArray *c3_m0 = NULL;
  sf_aircraft_ModeType c3_b_hoistedGlobal;
  const mxArray *c3_d_y = NULL;
  int32_T c3_c_u;
  const mxArray *c3_e_y = NULL;
  const mxArray *c3_m1 = NULL;
  sf_aircraft_ModeType c3_c_hoistedGlobal;
  const mxArray *c3_f_y = NULL;
  int32_T c3_d_u;
  const mxArray *c3_g_y = NULL;
  const mxArray *c3_m2 = NULL;
  sf_aircraft_ModeType c3_d_hoistedGlobal;
  const mxArray *c3_h_y = NULL;
  int32_T c3_e_u;
  const mxArray *c3_i_y = NULL;
  const mxArray *c3_m3 = NULL;
  int32_T c3_e_hoistedGlobal;
  const mxArray *c3_j_y = NULL;
  int32_T c3_f_hoistedGlobal;
  const mxArray *c3_k_y = NULL;
  int32_T c3_g_hoistedGlobal;
  const mxArray *c3_l_y = NULL;
  int32_T c3_h_hoistedGlobal;
  const mxArray *c3_m_y = NULL;
  uint8_T c3_i_hoistedGlobal;
  const mxArray *c3_n_y = NULL;
  uint8_T c3_j_hoistedGlobal;
  const mxArray *c3_o_y = NULL;
  uint8_T c3_k_hoistedGlobal;
  const mxArray *c3_p_y = NULL;
  uint8_T c3_l_hoistedGlobal;
  const mxArray *c3_q_y = NULL;
  uint8_T c3_m_hoistedGlobal;
  const mxArray *c3_r_y = NULL;
  uint8_T c3_n_hoistedGlobal;
  const mxArray *c3_s_y = NULL;
  uint8_T c3_o_hoistedGlobal;
  const mxArray *c3_t_y = NULL;
  uint8_T c3_p_hoistedGlobal;
  const mxArray *c3_u_y = NULL;
  uint8_T c3_q_hoistedGlobal;
  const mxArray *c3_v_y = NULL;
  uint8_T c3_r_hoistedGlobal;
  const mxArray *c3_w_y = NULL;
  c3_st = NULL;
  c3_st = NULL;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_createcellmatrix(18, 1), false);
  c3_hoistedGlobal = *chartInstance->c3_LI_mode;
  c3_b_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv0, c3_iv0);
  c3_b_u = (int32_T)c3_hoistedGlobal;
  c3_c_y = NULL;
  sf_mex_assign(&c3_c_y, sf_mex_create("y", &c3_b_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m0, c3_c_y, false);
  sf_mex_assign(&c3_b_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m0),
                false);
  sf_mex_destroy(&c3_m0);
  sf_mex_setcell(c3_y, 0, c3_b_y);
  c3_b_hoistedGlobal = *chartInstance->c3_LO_mode;
  c3_d_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv0, c3_iv0);
  c3_c_u = (int32_T)c3_b_hoistedGlobal;
  c3_e_y = NULL;
  sf_mex_assign(&c3_e_y, sf_mex_create("y", &c3_c_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m1, c3_e_y, false);
  sf_mex_assign(&c3_d_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m1),
                false);
  sf_mex_destroy(&c3_m1);
  sf_mex_setcell(c3_y, 1, c3_d_y);
  c3_c_hoistedGlobal = *chartInstance->c3_RI_mode;
  c3_f_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv0, c3_iv0);
  c3_d_u = (int32_T)c3_c_hoistedGlobal;
  c3_g_y = NULL;
  sf_mex_assign(&c3_g_y, sf_mex_create("y", &c3_d_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m2, c3_g_y, false);
  sf_mex_assign(&c3_f_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m2),
                false);
  sf_mex_destroy(&c3_m2);
  sf_mex_setcell(c3_y, 2, c3_f_y);
  c3_d_hoistedGlobal = *chartInstance->c3_RO_mode;
  c3_h_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv0, c3_iv0);
  c3_e_u = (int32_T)c3_d_hoistedGlobal;
  c3_i_y = NULL;
  sf_mex_assign(&c3_i_y, sf_mex_create("y", &c3_e_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m3, c3_i_y, false);
  sf_mex_assign(&c3_h_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m3),
                false);
  sf_mex_destroy(&c3_m3);
  sf_mex_setcell(c3_y, 3, c3_h_y);
  c3_e_hoistedGlobal = chartInstance->c3_fails;
  c3_j_y = NULL;
  sf_mex_assign(&c3_j_y, sf_mex_create("y", &c3_e_hoistedGlobal, 6, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 4, c3_j_y);
  c3_f_hoistedGlobal = chartInstance->c3_b_fails;
  c3_k_y = NULL;
  sf_mex_assign(&c3_k_y, sf_mex_create("y", &c3_f_hoistedGlobal, 6, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 5, c3_k_y);
  c3_g_hoistedGlobal = chartInstance->c3_c_fails;
  c3_l_y = NULL;
  sf_mex_assign(&c3_l_y, sf_mex_create("y", &c3_g_hoistedGlobal, 6, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 6, c3_l_y);
  c3_h_hoistedGlobal = chartInstance->c3_d_fails;
  c3_m_y = NULL;
  sf_mex_assign(&c3_m_y, sf_mex_create("y", &c3_h_hoistedGlobal, 6, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 7, c3_m_y);
  c3_i_hoistedGlobal = chartInstance->c3_is_active_c3_sf_aircraft_fault;
  c3_n_y = NULL;
  sf_mex_assign(&c3_n_y, sf_mex_create("y", &c3_i_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 8, c3_n_y);
  c3_j_hoistedGlobal = chartInstance->c3_is_active_LO;
  c3_o_y = NULL;
  sf_mex_assign(&c3_o_y, sf_mex_create("y", &c3_j_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 9, c3_o_y);
  c3_k_hoistedGlobal = chartInstance->c3_is_active_RO;
  c3_p_y = NULL;
  sf_mex_assign(&c3_p_y, sf_mex_create("y", &c3_k_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 10, c3_p_y);
  c3_l_hoistedGlobal = chartInstance->c3_is_active_LI;
  c3_q_y = NULL;
  sf_mex_assign(&c3_q_y, sf_mex_create("y", &c3_l_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 11, c3_q_y);
  c3_m_hoistedGlobal = chartInstance->c3_is_active_RI;
  c3_r_y = NULL;
  sf_mex_assign(&c3_r_y, sf_mex_create("y", &c3_m_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 12, c3_r_y);
  c3_n_hoistedGlobal = chartInstance->c3_is_c3_sf_aircraft_fault;
  c3_s_y = NULL;
  sf_mex_assign(&c3_s_y, sf_mex_create("y", &c3_n_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 13, c3_s_y);
  c3_o_hoistedGlobal = chartInstance->c3_is_LO;
  c3_t_y = NULL;
  sf_mex_assign(&c3_t_y, sf_mex_create("y", &c3_o_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 14, c3_t_y);
  c3_p_hoistedGlobal = chartInstance->c3_is_RO;
  c3_u_y = NULL;
  sf_mex_assign(&c3_u_y, sf_mex_create("y", &c3_p_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 15, c3_u_y);
  c3_q_hoistedGlobal = chartInstance->c3_is_LI;
  c3_v_y = NULL;
  sf_mex_assign(&c3_v_y, sf_mex_create("y", &c3_q_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 16, c3_v_y);
  c3_r_hoistedGlobal = chartInstance->c3_is_RI;
  c3_w_y = NULL;
  sf_mex_assign(&c3_w_y, sf_mex_create("y", &c3_r_hoistedGlobal, 3, 0U, 0U, 0U,
    0), false);
  sf_mex_setcell(c3_y, 17, c3_w_y);
  sf_mex_assign(&c3_st, c3_y, false);
  return c3_st;
}

static void set_sim_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray *c3_st)
{
  const mxArray *c3_b_u;
  c3_b_u = sf_mex_dup(c3_st);
  *chartInstance->c3_LI_mode = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 0)), "LI_mode");
  *chartInstance->c3_LO_mode = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 1)), "LO_mode");
  *chartInstance->c3_RI_mode = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 2)), "RI_mode");
  *chartInstance->c3_RO_mode = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 3)), "RO_mode");
  chartInstance->c3_fails = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 4)), "fails");
  chartInstance->c3_b_fails = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 5)), "fails");
  chartInstance->c3_c_fails = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 6)), "fails");
  chartInstance->c3_d_fails = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 7)), "fails");
  chartInstance->c3_is_active_c3_sf_aircraft_fault = c3_c_emlrt_marshallIn
    (chartInstance, sf_mex_dup(sf_mex_getcell(c3_b_u, 8)),
     "is_active_c3_sf_aircraft_fault");
  chartInstance->c3_is_active_LO = c3_c_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 9)), "is_active_LO");
  chartInstance->c3_is_active_RO = c3_c_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 10)), "is_active_RO");
  chartInstance->c3_is_active_LI = c3_c_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 11)), "is_active_LI");
  chartInstance->c3_is_active_RI = c3_c_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 12)), "is_active_RI");
  chartInstance->c3_is_c3_sf_aircraft_fault = c3_c_emlrt_marshallIn
    (chartInstance, sf_mex_dup(sf_mex_getcell(c3_b_u, 13)),
     "is_c3_sf_aircraft_fault");
  chartInstance->c3_is_LO = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 14)), "is_LO");
  chartInstance->c3_is_RO = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 15)), "is_RO");
  chartInstance->c3_is_LI = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 16)), "is_LI");
  chartInstance->c3_is_RI = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 17)), "is_RI");
  sf_mex_assign(&chartInstance->c3_setSimStateSideEffectsInfo,
                c3_i_emlrt_marshallIn(chartInstance, sf_mex_dup(sf_mex_getcell
    (c3_b_u, 18)), "setSimStateSideEffectsInfo"), true);
  sf_mex_destroy(&c3_b_u);
  chartInstance->c3_doSetSimStateSideEffects = 1U;
  c3_update_debugger_state_c3_sf_aircraft_fault(chartInstance);
  sf_mex_destroy(&c3_st);
}

static void c3_set_sim_state_side_effects_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  if (chartInstance->c3_doSetSimStateSideEffects != 0) {
    if (chartInstance->c3_is_c3_sf_aircraft_fault == c3_IN_Actuators) {
      chartInstance->c3_tp_Actuators = 1U;
    } else {
      chartInstance->c3_tp_Actuators = 0U;
    }

    if (chartInstance->c3_is_active_LO == 1U) {
      chartInstance->c3_tp_LO = 1U;
    } else {
      chartInstance->c3_tp_LO = 0U;
    }

    if (chartInstance->c3_is_LO == c3_IN_Isolated) {
      chartInstance->c3_tp_Isolated = 1U;
    } else {
      chartInstance->c3_tp_Isolated = 0U;
    }

    if (chartInstance->c3_is_LO == c3_IN_L1) {
      chartInstance->c3_tp_L1 = 1U;
    } else {
      chartInstance->c3_tp_L1 = 0U;
    }

    if (*chartInstance->c3_LO_mode == Active) {
      chartInstance->c3_tp_Active = 1U;
    } else {
      chartInstance->c3_tp_Active = 0U;
    }

    if (*chartInstance->c3_LO_mode == Off) {
      chartInstance->c3_tp_Off = 1U;
    } else {
      chartInstance->c3_tp_Off = 0U;
    }

    if (*chartInstance->c3_LO_mode == Passive) {
      chartInstance->c3_tp_Passive = 1U;
    } else {
      chartInstance->c3_tp_Passive = 0U;
    }

    if (*chartInstance->c3_LO_mode == Standby) {
      chartInstance->c3_tp_Standby = 1U;
    } else {
      chartInstance->c3_tp_Standby = 0U;
    }

    if (chartInstance->c3_is_active_RO == 1U) {
      chartInstance->c3_tp_RO = 1U;
    } else {
      chartInstance->c3_tp_RO = 0U;
    }

    if (chartInstance->c3_is_RO == c3_IN_Isolated) {
      chartInstance->c3_b_tp_Isolated = 1U;
    } else {
      chartInstance->c3_b_tp_Isolated = 0U;
    }

    if (chartInstance->c3_is_RO == c3_IN_L1) {
      chartInstance->c3_b_tp_L1 = 1U;
    } else {
      chartInstance->c3_b_tp_L1 = 0U;
    }

    if (*chartInstance->c3_RO_mode == Active) {
      chartInstance->c3_b_tp_Active = 1U;
    } else {
      chartInstance->c3_b_tp_Active = 0U;
    }

    if (*chartInstance->c3_RO_mode == Off) {
      chartInstance->c3_b_tp_Off = 1U;
    } else {
      chartInstance->c3_b_tp_Off = 0U;
    }

    if (*chartInstance->c3_RO_mode == Passive) {
      chartInstance->c3_b_tp_Passive = 1U;
    } else {
      chartInstance->c3_b_tp_Passive = 0U;
    }

    if (*chartInstance->c3_RO_mode == Standby) {
      chartInstance->c3_b_tp_Standby = 1U;
    } else {
      chartInstance->c3_b_tp_Standby = 0U;
    }

    if (chartInstance->c3_is_active_LI == 1U) {
      chartInstance->c3_tp_LI = 1U;
    } else {
      chartInstance->c3_tp_LI = 0U;
    }

    if (chartInstance->c3_is_LI == c3_IN_Isolated) {
      chartInstance->c3_c_tp_Isolated = 1U;
    } else {
      chartInstance->c3_c_tp_Isolated = 0U;
    }

    if (chartInstance->c3_is_LI == c3_IN_L1) {
      chartInstance->c3_c_tp_L1 = 1U;
    } else {
      chartInstance->c3_c_tp_L1 = 0U;
    }

    if (*chartInstance->c3_LI_mode == Active) {
      chartInstance->c3_c_tp_Active = 1U;
    } else {
      chartInstance->c3_c_tp_Active = 0U;
    }

    if (*chartInstance->c3_LI_mode == Off) {
      chartInstance->c3_c_tp_Off = 1U;
    } else {
      chartInstance->c3_c_tp_Off = 0U;
    }

    if (*chartInstance->c3_LI_mode == Passive) {
      chartInstance->c3_c_tp_Passive = 1U;
    } else {
      chartInstance->c3_c_tp_Passive = 0U;
    }

    if (*chartInstance->c3_LI_mode == Standby) {
      chartInstance->c3_c_tp_Standby = 1U;
    } else {
      chartInstance->c3_c_tp_Standby = 0U;
    }

    if (chartInstance->c3_is_active_RI == 1U) {
      chartInstance->c3_tp_RI = 1U;
    } else {
      chartInstance->c3_tp_RI = 0U;
    }

    if (chartInstance->c3_is_RI == c3_IN_Isolated) {
      chartInstance->c3_d_tp_Isolated = 1U;
    } else {
      chartInstance->c3_d_tp_Isolated = 0U;
    }

    if (chartInstance->c3_is_RI == c3_IN_L1) {
      chartInstance->c3_d_tp_L1 = 1U;
    } else {
      chartInstance->c3_d_tp_L1 = 0U;
    }

    if (*chartInstance->c3_RI_mode == Active) {
      chartInstance->c3_d_tp_Active = 1U;
    } else {
      chartInstance->c3_d_tp_Active = 0U;
    }

    if (*chartInstance->c3_RI_mode == Off) {
      chartInstance->c3_d_tp_Off = 1U;
    } else {
      chartInstance->c3_d_tp_Off = 0U;
    }

    if (*chartInstance->c3_RI_mode == Passive) {
      chartInstance->c3_d_tp_Passive = 1U;
    } else {
      chartInstance->c3_d_tp_Passive = 0U;
    }

    if (*chartInstance->c3_RI_mode == Standby) {
      chartInstance->c3_d_tp_Standby = 1U;
    } else {
      chartInstance->c3_d_tp_Standby = 0U;
    }

    chartInstance->c3_doSetSimStateSideEffects = 0U;
  }
}

static void finalize_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  sf_mex_destroy(&chartInstance->c3_setSimStateSideEffectsInfo);
}

static void sf_gateway_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  c3_set_sim_state_side_effects_c3_sf_aircraft_fault(chartInstance);
  _SFD_SYMBOL_SCOPE_PUSH(0U, 0U);
  _sfTime_ = sf_get_time(chartInstance->S);
  _SFD_CC_CALL(CHART_ENTER_SFUNCTION_TAG, 0U, chartInstance->c3_sfEvent);
  chartInstance->c3_sfEvent = CALL_EVENT;
  c3_c3_sf_aircraft_fault(chartInstance);
  _SFD_SYMBOL_SCOPE_POP();
}

static void mdl_start_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct *
  chartInstance)
{
  c3_init_sf_message_store_memory(chartInstance);
  sim_mode_is_external(chartInstance->S);
}

static void c3_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  _SFD_CC_CALL(CHART_ENTER_DURING_FUNCTION_TAG, 0U, chartInstance->c3_sfEvent);
  if (chartInstance->c3_is_active_c3_sf_aircraft_fault == 0U) {
    _SFD_CC_CALL(CHART_ENTER_ENTRY_FUNCTION_TAG, 0U, chartInstance->c3_sfEvent);
    chartInstance->c3_is_active_c3_sf_aircraft_fault = 1U;
    _SFD_CC_CALL(EXIT_OUT_OF_FUNCTION_TAG, 0U, chartInstance->c3_sfEvent);
    if (chartInstance->c3_is_c3_sf_aircraft_fault == c3_IN_Actuators) {
    } else {
      chartInstance->c3_is_c3_sf_aircraft_fault = c3_IN_Actuators;
      _SFD_CS_CALL(STATE_ACTIVE_TAG, 0U, chartInstance->c3_sfEvent);
      chartInstance->c3_tp_Actuators = 1U;
      c3_L_switch(chartInstance);
      c3_R_switch(chartInstance);
    }

    chartInstance->c3_is_active_LO = 1U;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 8U, chartInstance->c3_sfEvent);
    chartInstance->c3_tp_LO = 1U;
    chartInstance->c3_fails = 0;
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_fails, 0U);
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 10U, chartInstance->c3_sfEvent);
    chartInstance->c3_is_LO = c3_IN_L1;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 10U, chartInstance->c3_sfEvent);
    chartInstance->c3_tp_L1 = 1U;
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 15U, chartInstance->c3_sfEvent);
    *chartInstance->c3_LO_mode = Passive;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
    chartInstance->c3_tp_Passive = 1U;
    chartInstance->c3_is_active_RO = 1U;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 22U, chartInstance->c3_sfEvent);
    chartInstance->c3_tp_RO = 1U;
    chartInstance->c3_b_fails = 0;
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_b_fails, 1U);
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 47U, chartInstance->c3_sfEvent);
    chartInstance->c3_is_RO = c3_IN_L1;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 24U, chartInstance->c3_sfEvent);
    chartInstance->c3_b_tp_L1 = 1U;
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 50U, chartInstance->c3_sfEvent);
    *chartInstance->c3_RO_mode = Passive;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
    chartInstance->c3_b_tp_Passive = 1U;
    chartInstance->c3_is_active_LI = 1U;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 1U, chartInstance->c3_sfEvent);
    chartInstance->c3_tp_LI = 1U;
    chartInstance->c3_c_fails = 0;
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_c_fails, 2U);
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 5U, chartInstance->c3_sfEvent);
    chartInstance->c3_is_LI = c3_IN_L1;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
    chartInstance->c3_c_tp_L1 = 1U;
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 1U, chartInstance->c3_sfEvent);
    *chartInstance->c3_LI_mode = Passive;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
    chartInstance->c3_c_tp_Passive = 1U;
    chartInstance->c3_is_active_RI = 1U;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 15U, chartInstance->c3_sfEvent);
    chartInstance->c3_tp_RI = 1U;
    chartInstance->c3_d_fails = 0;
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_d_fails, 3U);
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 38U, chartInstance->c3_sfEvent);
    chartInstance->c3_is_RI = c3_IN_L1;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 17U, chartInstance->c3_sfEvent);
    chartInstance->c3_d_tp_L1 = 1U;
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 35U, chartInstance->c3_sfEvent);
    *chartInstance->c3_RI_mode = Passive;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
    chartInstance->c3_d_tp_Passive = 1U;
    if ((chartInstance->c3_is_active_c3_sf_aircraft_fault == 1U) &&
        (!(chartInstance->c3_is_c3_sf_aircraft_fault == c3_IN_Actuators))) {
      sf_state_inconsistency_error(chartInstance->S, 0);
    }
  } else if (chartInstance->c3_is_c3_sf_aircraft_fault != c3_IN_Actuators) {
  } else {
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 0U, chartInstance->c3_sfEvent);
    c3_L_switch(chartInstance);
    c3_R_switch(chartInstance);
    if (chartInstance->c3_is_active_LO == 0U) {
    } else {
      c3_LO(chartInstance);
    }

    if (chartInstance->c3_is_active_RO == 0U) {
    } else {
      c3_RO(chartInstance);
    }

    if (chartInstance->c3_is_active_LI == 0U) {
    } else {
      c3_LI(chartInstance);
    }

    if (chartInstance->c3_is_active_RI == 0U) {
    } else {
      c3_RI(chartInstance);
    }

    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 0U, chartInstance->c3_sfEvent);
  }

  _SFD_CC_CALL(EXIT_OUT_OF_FUNCTION_TAG, 0U, chartInstance->c3_sfEvent);
}

static void initSimStructsc3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void c3_LO(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 8U, chartInstance->c3_sfEvent);
  switch (chartInstance->c3_is_LO) {
   case c3_IN_Isolated:
    CV_STATE_EVAL(8, 0, c3_IN_Isolated);
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 9U, chartInstance->c3_sfEvent);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 9U, chartInstance->c3_sfEvent);
    break;

   case c3_IN_L1:
    CV_STATE_EVAL(8, 0, c3_IN_L1);
    c3_L1(chartInstance);
    break;

   default:
    CV_STATE_EVAL(8, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_LO = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
    break;
  }

  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 8U, chartInstance->c3_sfEvent);
}

static void c3_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  real_T c3_d0;
  real_T c3_d1;
  boolean_T c3_d_out;
  boolean_T c3_e_out;
  real_T c3_d2;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  real_T c3_d3;
  real_T c3_d4;
  boolean_T c3_f_out;
  int32_T c3_b_previousEvent;
  real_T c3_d5;
  boolean_T c3_g_out;
  boolean_T c3_d_temp;
  real_T c3_d6;
  boolean_T c3_h_out;
  _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 9U, chartInstance->c3_sfEvent);
  c3_out = (CV_TRANSITION_EVAL(9U, (int32_T)_SFD_CCP_CALL(5U, 9U, 0,
              (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U,
              chartInstance->c3_sfEvent)) != 0);
  if (c3_out) {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
    c3_exit_internal_L1(chartInstance);
    chartInstance->c3_tp_L1 = 0U;
    chartInstance->c3_is_LO = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 10U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 9U,
                 chartInstance->c3_sfEvent);
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    if (chartInstance->c3_is_active_LI == 0U) {
    } else {
      c3_LI(chartInstance);
    }

    _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    chartInstance->c3_sfEvent = c3_previousEvent;
    if (chartInstance->c3_is_LO == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_LO == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
    }

    if (chartInstance->c3_is_LO == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_LO == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
      } else {
        chartInstance->c3_is_LO = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
        chartInstance->c3_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 10U, chartInstance->c3_sfEvent);
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
    }
  } else {
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 10U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 11U,
                 chartInstance->c3_sfEvent);
    c3_temp = _SFD_CCP_CALL(5U, 11U, 0, (chartInstance->c3_sfEvent ==
      c3_event_go_off) != 0U, chartInstance->c3_sfEvent);
    if (c3_temp) {
      c3_temp = !_SFD_CCP_CALL(5U, 11U, 1, (*chartInstance->c3_LO_mode == Off)
        != 0U, chartInstance->c3_sfEvent);
    }

    c3_b_out = (CV_TRANSITION_EVAL(11U, (int32_T)c3_temp) != 0);
    if (c3_b_out) {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 14U,
                   chartInstance->c3_sfEvent);
      c3_c_out = (CV_TRANSITION_EVAL(14U, (int32_T)_SFD_CCP_CALL(5U, 14U, 0,
        (boolean_T)CV_RELATIONAL_EVAL(5U, 14U, 0, (real_T)
        chartInstance->c3_fails, 5.0, 0, 5U, chartInstance->c3_fails >= 5) != 0U,
        chartInstance->c3_sfEvent)) != 0);
      if (c3_c_out) {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 14U, chartInstance->c3_sfEvent);
        c3_exit_internal_L1(chartInstance);
        chartInstance->c3_tp_L1 = 0U;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 10U, chartInstance->c3_sfEvent);
        chartInstance->c3_is_LO = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 9U, chartInstance->c3_sfEvent);
        chartInstance->c3_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 10U, chartInstance->c3_sfEvent);
      } else {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
        c3_exit_internal_L1(chartInstance);
        _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 27U,
                     chartInstance->c3_sfEvent);
        c3_b_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_LI == 0U) {
        } else {
          c3_LI(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_b_previousEvent;
        if (*chartInstance->c3_LO_mode == Isolated) {
          if (chartInstance->c3_is_LO != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
        }

        if (*chartInstance->c3_LO_mode == Isolated) {
          if (chartInstance->c3_is_LO != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
          } else {
            *chartInstance->c3_LO_mode = Off;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 12U, chartInstance->c3_sfEvent);
            chartInstance->c3_tp_Off = 1U;
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 10U,
                         chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
        }
      }
    } else {
      switch (*chartInstance->c3_LO_mode) {
       case Passive:
        CV_STATE_EVAL(10, 0, 3);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 18U,
                     chartInstance->c3_sfEvent);
        c3_d0 = c3_LI_act(chartInstance);
        c3_e_out = (CV_TRANSITION_EVAL(18U, (int32_T)_SFD_CCP_CALL(5U, 18U, 0,
          (c3_d0 != 0.0) != 0U, chartInstance->c3_sfEvent)) != 0);
        if (c3_e_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
          chartInstance->c3_tp_Passive = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LO_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 14U, chartInstance->c3_sfEvent);
          chartInstance->c3_tp_Standby = 1U;
        } else {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 17U,
                       chartInstance->c3_sfEvent);
          c3_d5 = c3_LI_act(chartInstance);
          c3_d_temp = !_SFD_CCP_CALL(5U, 17U, 0, (c3_d5 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
          if (!c3_d_temp) {
            c3_d6 = c3_RO_act(chartInstance);
            c3_d_temp = _SFD_CCP_CALL(5U, 17U, 1, (c3_d6 != 0.0) != 0U,
              chartInstance->c3_sfEvent);
          }

          c3_h_out = (CV_TRANSITION_EVAL(17U, (int32_T)c3_d_temp) != 0);
          if (c3_h_out) {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 17U, chartInstance->c3_sfEvent);
            chartInstance->c3_tp_Passive = 0U;
            _SFD_CS_CALL(STATE_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
            *chartInstance->c3_LO_mode = Active;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
            chartInstance->c3_tp_Active = 1U;
          } else {
            _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 13U,
                         chartInstance->c3_sfEvent);
          }
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 13U, chartInstance->c3_sfEvent);
        break;

       case Standby:
        CV_STATE_EVAL(10, 0, 4);
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 19U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 17U,
                     chartInstance->c3_sfEvent);
        c3_d2 = c3_LI_act(chartInstance);
        c3_c_temp = !_SFD_CCP_CALL(5U, 17U, 0, (c3_d2 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (!c3_c_temp) {
          c3_d4 = c3_RO_act(chartInstance);
          c3_c_temp = _SFD_CCP_CALL(5U, 17U, 1, (c3_d4 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_g_out = (CV_TRANSITION_EVAL(17U, (int32_T)c3_c_temp) != 0);
        if (c3_g_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 17U, chartInstance->c3_sfEvent);
          chartInstance->c3_tp_Standby = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 14U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LO_mode = Active;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
          chartInstance->c3_tp_Active = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 14U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 14U, chartInstance->c3_sfEvent);
        break;

       case Active:
        CV_STATE_EVAL(10, 0, 1);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 16U,
                     chartInstance->c3_sfEvent);
        c3_d1 = c3_RO_act(chartInstance);
        c3_b_temp = !_SFD_CCP_CALL(5U, 16U, 0, (c3_d1 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (c3_b_temp) {
          c3_d3 = c3_LI_act(chartInstance);
          c3_b_temp = _SFD_CCP_CALL(5U, 16U, 1, (c3_d3 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_f_out = (CV_TRANSITION_EVAL(16U, (int32_T)c3_b_temp) != 0);
        if (c3_f_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 16U, chartInstance->c3_sfEvent);
          chartInstance->c3_tp_Active = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LO_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 14U, chartInstance->c3_sfEvent);
          chartInstance->c3_tp_Standby = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 11U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 11U, chartInstance->c3_sfEvent);
        break;

       case Off:
        CV_STATE_EVAL(10, 0, 2);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 12U,
                     chartInstance->c3_sfEvent);
        c3_d_out = (CV_TRANSITION_EVAL(12U, !_SFD_CCP_CALL(5U, 12U, 0,
          ((boolean_T *)&((char_T *)chartInstance->c3_u)[72])[0] != 0U,
          chartInstance->c3_sfEvent)) != 0);
        if (c3_d_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 12U, chartInstance->c3_sfEvent);
          if (*chartInstance->c3_LO_mode != Off) {
          } else {
            chartInstance->c3_tp_Off = 0U;
            _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 12U,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_fails = c3__s32_add__(chartInstance,
              chartInstance->c3_fails, 1, 36U, 7, 7);
            _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_fails, 0U);
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 12U,
                         chartInstance->c3_sfEvent);
            *chartInstance->c3_LO_mode = Isolated;
            _SFD_CS_CALL(STATE_INACTIVE_TAG, 12U, chartInstance->c3_sfEvent);
          }

          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 15U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LO_mode = Passive;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
          chartInstance->c3_tp_Passive = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 12U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 12U, chartInstance->c3_sfEvent);
        break;

       default:
        CV_STATE_EVAL(10, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_LO_mode = Isolated;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
        break;
      }

      _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 10U, chartInstance->c3_sfEvent);
    }
  }
}

static void c3_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  switch (*chartInstance->c3_LO_mode) {
   case Active:
    CV_STATE_EVAL(10, 1, 1);
    chartInstance->c3_tp_Active = 0U;
    *chartInstance->c3_LO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
    break;

   case Off:
    CV_STATE_EVAL(10, 1, 2);
    chartInstance->c3_tp_Off = 0U;
    _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 12U, chartInstance->c3_sfEvent);
    chartInstance->c3_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_fails, 1, 36U, 7, 7);
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_fails, 0U);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 12U, chartInstance->c3_sfEvent);
    *chartInstance->c3_LO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 12U, chartInstance->c3_sfEvent);
    break;

   case Passive:
    CV_STATE_EVAL(10, 1, 3);
    chartInstance->c3_tp_Passive = 0U;
    *chartInstance->c3_LO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
    break;

   case Standby:
    CV_STATE_EVAL(10, 1, 4);
    chartInstance->c3_tp_Standby = 0U;
    *chartInstance->c3_LO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 14U, chartInstance->c3_sfEvent);
    break;

   default:
    CV_STATE_EVAL(10, 1, 0);
    *chartInstance->c3_LO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 11U, chartInstance->c3_sfEvent);
    break;
  }
}

static void c3_RO(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 22U, chartInstance->c3_sfEvent);
  switch (chartInstance->c3_is_RO) {
   case c3_IN_Isolated:
    CV_STATE_EVAL(22, 0, c3_IN_Isolated);
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 23U, chartInstance->c3_sfEvent);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 23U, chartInstance->c3_sfEvent);
    break;

   case c3_IN_L1:
    CV_STATE_EVAL(22, 0, c3_IN_L1);
    c3_b_L1(chartInstance);
    break;

   default:
    CV_STATE_EVAL(22, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_RO = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 23U, chartInstance->c3_sfEvent);
    break;
  }

  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 22U, chartInstance->c3_sfEvent);
}

static void c3_b_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  real_T c3_d7;
  real_T c3_d8;
  boolean_T c3_d_out;
  boolean_T c3_e_out;
  real_T c3_d9;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  real_T c3_d10;
  real_T c3_d11;
  boolean_T c3_f_out;
  int32_T c3_b_previousEvent;
  real_T c3_d12;
  boolean_T c3_g_out;
  boolean_T c3_d_temp;
  real_T c3_d13;
  boolean_T c3_h_out;
  _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 49U, chartInstance->c3_sfEvent);
  c3_out = (CV_TRANSITION_EVAL(49U, (int32_T)_SFD_CCP_CALL(5U, 49U, 0,
              (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U,
              chartInstance->c3_sfEvent)) != 0);
  if (c3_out) {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 49U, chartInstance->c3_sfEvent);
    c3_b_exit_internal_L1(chartInstance);
    chartInstance->c3_b_tp_L1 = 0U;
    chartInstance->c3_is_RO = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 24U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 49U,
                 chartInstance->c3_sfEvent);
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    if (chartInstance->c3_is_active_RI == 0U) {
    } else {
      c3_RI(chartInstance);
    }

    _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    chartInstance->c3_sfEvent = c3_previousEvent;
    if (chartInstance->c3_is_RO == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_RO == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 49U, chartInstance->c3_sfEvent);
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 49U, chartInstance->c3_sfEvent);
    }

    if (chartInstance->c3_is_RO == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_RO == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 49U, chartInstance->c3_sfEvent);
      } else {
        chartInstance->c3_is_RO = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 23U, chartInstance->c3_sfEvent);
        chartInstance->c3_b_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 24U, chartInstance->c3_sfEvent);
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 49U, chartInstance->c3_sfEvent);
    }
  } else {
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 24U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 21U,
                 chartInstance->c3_sfEvent);
    c3_temp = _SFD_CCP_CALL(5U, 21U, 0, (chartInstance->c3_sfEvent ==
      c3_event_go_off) != 0U, chartInstance->c3_sfEvent);
    if (c3_temp) {
      c3_temp = !_SFD_CCP_CALL(5U, 21U, 1, (*chartInstance->c3_RO_mode == Off)
        != 0U, chartInstance->c3_sfEvent);
    }

    c3_b_out = (CV_TRANSITION_EVAL(21U, (int32_T)c3_temp) != 0);
    if (c3_b_out) {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 21U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 48U,
                   chartInstance->c3_sfEvent);
      c3_c_out = (CV_TRANSITION_EVAL(48U, (int32_T)_SFD_CCP_CALL(5U, 48U, 0,
        (boolean_T)CV_RELATIONAL_EVAL(5U, 48U, 0, (real_T)
        chartInstance->c3_b_fails, 5.0, 0, 5U, chartInstance->c3_b_fails >= 5)
        != 0U, chartInstance->c3_sfEvent)) != 0);
      if (c3_c_out) {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 48U, chartInstance->c3_sfEvent);
        c3_b_exit_internal_L1(chartInstance);
        chartInstance->c3_b_tp_L1 = 0U;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 24U, chartInstance->c3_sfEvent);
        chartInstance->c3_is_RO = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 23U, chartInstance->c3_sfEvent);
        chartInstance->c3_b_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 24U, chartInstance->c3_sfEvent);
      } else {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
        c3_b_exit_internal_L1(chartInstance);
        _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 20U,
                     chartInstance->c3_sfEvent);
        c3_b_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_RI == 0U) {
        } else {
          c3_RI(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_b_previousEvent;
        if (*chartInstance->c3_RO_mode == Isolated) {
          if (chartInstance->c3_is_RO != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
        }

        if (*chartInstance->c3_RO_mode == Isolated) {
          if (chartInstance->c3_is_RO != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
          } else {
            *chartInstance->c3_RO_mode = Off;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 26U, chartInstance->c3_sfEvent);
            chartInstance->c3_b_tp_Off = 1U;
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 24U,
                         chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
        }
      }
    } else {
      switch (*chartInstance->c3_RO_mode) {
       case Passive:
        CV_STATE_EVAL(24, 0, 3);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 23U,
                     chartInstance->c3_sfEvent);
        c3_d7 = c3_RI_act(chartInstance);
        c3_e_out = (CV_TRANSITION_EVAL(23U, (int32_T)_SFD_CCP_CALL(5U, 23U, 0,
          (c3_d7 != 0.0) != 0U, chartInstance->c3_sfEvent)) != 0);
        if (c3_e_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 23U, chartInstance->c3_sfEvent);
          chartInstance->c3_b_tp_Passive = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
          *chartInstance->c3_RO_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 28U, chartInstance->c3_sfEvent);
          chartInstance->c3_b_tp_Standby = 1U;
        } else {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 51U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 0U,
                       chartInstance->c3_sfEvent);
          c3_d12 = c3_RI_act(chartInstance);
          c3_d_temp = !_SFD_CCP_CALL(5U, 0U, 0, (c3_d12 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
          if (!c3_d_temp) {
            c3_d13 = c3_LO_act(chartInstance);
            c3_d_temp = _SFD_CCP_CALL(5U, 0U, 1, (c3_d13 != 0.0) != 0U,
              chartInstance->c3_sfEvent);
          }

          c3_h_out = (CV_TRANSITION_EVAL(0U, (int32_T)c3_d_temp) != 0);
          if (c3_h_out) {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 0U, chartInstance->c3_sfEvent);
            chartInstance->c3_b_tp_Passive = 0U;
            _SFD_CS_CALL(STATE_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
            *chartInstance->c3_RO_mode = Active;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
            chartInstance->c3_b_tp_Active = 1U;
          } else {
            _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 27U,
                         chartInstance->c3_sfEvent);
          }
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 27U, chartInstance->c3_sfEvent);
        break;

       case Standby:
        CV_STATE_EVAL(24, 0, 4);
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 2U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 0U,
                     chartInstance->c3_sfEvent);
        c3_d9 = c3_RI_act(chartInstance);
        c3_c_temp = !_SFD_CCP_CALL(5U, 0U, 0, (c3_d9 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (!c3_c_temp) {
          c3_d11 = c3_LO_act(chartInstance);
          c3_c_temp = _SFD_CCP_CALL(5U, 0U, 1, (c3_d11 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_g_out = (CV_TRANSITION_EVAL(0U, (int32_T)c3_c_temp) != 0);
        if (c3_g_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 0U, chartInstance->c3_sfEvent);
          chartInstance->c3_b_tp_Standby = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 28U, chartInstance->c3_sfEvent);
          *chartInstance->c3_RO_mode = Active;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
          chartInstance->c3_b_tp_Active = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 28U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 28U, chartInstance->c3_sfEvent);
        break;

       case Active:
        CV_STATE_EVAL(24, 0, 1);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 22U,
                     chartInstance->c3_sfEvent);
        c3_d8 = c3_LO_act(chartInstance);
        c3_b_temp = !_SFD_CCP_CALL(5U, 22U, 0, (c3_d8 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (c3_b_temp) {
          c3_d10 = c3_RI_act(chartInstance);
          c3_b_temp = _SFD_CCP_CALL(5U, 22U, 1, (c3_d10 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_f_out = (CV_TRANSITION_EVAL(22U, (int32_T)c3_b_temp) != 0);
        if (c3_f_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 22U, chartInstance->c3_sfEvent);
          chartInstance->c3_b_tp_Active = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
          *chartInstance->c3_RO_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 28U, chartInstance->c3_sfEvent);
          chartInstance->c3_b_tp_Standby = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 25U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 25U, chartInstance->c3_sfEvent);
        break;

       case Off:
        CV_STATE_EVAL(24, 0, 2);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 7U,
                     chartInstance->c3_sfEvent);
        c3_d_out = (CV_TRANSITION_EVAL(7U, !_SFD_CCP_CALL(5U, 7U, 0, ((boolean_T
          *)&((char_T *)chartInstance->c3_u)[72])[2] != 0U,
          chartInstance->c3_sfEvent)) != 0);
        if (c3_d_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 7U, chartInstance->c3_sfEvent);
          if (*chartInstance->c3_RO_mode != Off) {
          } else {
            chartInstance->c3_b_tp_Off = 0U;
            _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 26U,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_b_fails = c3__s32_add__(chartInstance,
              chartInstance->c3_b_fails, 1, 20U, 7, 7);
            _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_b_fails, 1U);
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 26U,
                         chartInstance->c3_sfEvent);
            *chartInstance->c3_RO_mode = Isolated;
            _SFD_CS_CALL(STATE_INACTIVE_TAG, 26U, chartInstance->c3_sfEvent);
          }

          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 50U, chartInstance->c3_sfEvent);
          *chartInstance->c3_RO_mode = Passive;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
          chartInstance->c3_b_tp_Passive = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 26U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 26U, chartInstance->c3_sfEvent);
        break;

       default:
        CV_STATE_EVAL(24, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_RO_mode = Isolated;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
        break;
      }

      _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 24U, chartInstance->c3_sfEvent);
    }
  }
}

static void c3_b_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  switch (*chartInstance->c3_RO_mode) {
   case Active:
    CV_STATE_EVAL(24, 1, 1);
    chartInstance->c3_b_tp_Active = 0U;
    *chartInstance->c3_RO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
    break;

   case Off:
    CV_STATE_EVAL(24, 1, 2);
    chartInstance->c3_b_tp_Off = 0U;
    _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 26U, chartInstance->c3_sfEvent);
    chartInstance->c3_b_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_b_fails, 1, 20U, 7, 7);
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_b_fails, 1U);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 26U, chartInstance->c3_sfEvent);
    *chartInstance->c3_RO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 26U, chartInstance->c3_sfEvent);
    break;

   case Passive:
    CV_STATE_EVAL(24, 1, 3);
    chartInstance->c3_b_tp_Passive = 0U;
    *chartInstance->c3_RO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 27U, chartInstance->c3_sfEvent);
    break;

   case Standby:
    CV_STATE_EVAL(24, 1, 4);
    chartInstance->c3_b_tp_Standby = 0U;
    *chartInstance->c3_RO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 28U, chartInstance->c3_sfEvent);
    break;

   default:
    CV_STATE_EVAL(24, 1, 0);
    *chartInstance->c3_RO_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
    break;
  }
}

static void c3_LI(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 1U, chartInstance->c3_sfEvent);
  switch (chartInstance->c3_is_LI) {
   case c3_IN_Isolated:
    CV_STATE_EVAL(1, 0, c3_IN_Isolated);
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 2U, chartInstance->c3_sfEvent);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 2U, chartInstance->c3_sfEvent);
    break;

   case c3_IN_L1:
    CV_STATE_EVAL(1, 0, c3_IN_L1);
    c3_c_L1(chartInstance);
    break;

   default:
    CV_STATE_EVAL(1, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_LI = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 2U, chartInstance->c3_sfEvent);
    break;
  }

  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 1U, chartInstance->c3_sfEvent);
}

static void c3_c_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  real_T c3_d14;
  real_T c3_d15;
  boolean_T c3_d_out;
  boolean_T c3_e_out;
  real_T c3_d16;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  real_T c3_d17;
  real_T c3_d18;
  boolean_T c3_f_out;
  int32_T c3_b_previousEvent;
  real_T c3_d19;
  boolean_T c3_g_out;
  int32_T c3_c_previousEvent;
  boolean_T c3_d_temp;
  real_T c3_d20;
  boolean_T c3_h_out;
  int32_T c3_d_previousEvent;
  _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 3U, chartInstance->c3_sfEvent);
  c3_out = (CV_TRANSITION_EVAL(3U, (int32_T)_SFD_CCP_CALL(5U, 3U, 0,
              (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U,
              chartInstance->c3_sfEvent)) != 0);
  if (c3_out) {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
    c3_c_exit_internal_L1(chartInstance);
    chartInstance->c3_c_tp_L1 = 0U;
    chartInstance->c3_is_LI = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 3U,
                 chartInstance->c3_sfEvent);
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    if (chartInstance->c3_is_active_LO == 0U) {
    } else {
      c3_LO(chartInstance);
    }

    _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    chartInstance->c3_sfEvent = c3_previousEvent;
    if (chartInstance->c3_is_LI == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_LI == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
      } else {
        c3_c_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_RO == 0U) {
        } else {
          c3_RO(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_c_previousEvent;
        if (chartInstance->c3_is_LI == c3_IN_NO_ACTIVE_CHILD) {
          if (chartInstance->c3_is_active_LI == 0U) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
        }
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
    }

    if (chartInstance->c3_is_LI == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_LI == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
      } else {
        chartInstance->c3_is_LI = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 2U, chartInstance->c3_sfEvent);
        chartInstance->c3_c_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
    }
  } else {
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 41U,
                 chartInstance->c3_sfEvent);
    c3_temp = _SFD_CCP_CALL(5U, 41U, 0, (chartInstance->c3_sfEvent ==
      c3_event_go_off) != 0U, chartInstance->c3_sfEvent);
    if (c3_temp) {
      c3_temp = !_SFD_CCP_CALL(5U, 41U, 1, (*chartInstance->c3_LI_mode == Off)
        != 0U, chartInstance->c3_sfEvent);
    }

    c3_b_out = (CV_TRANSITION_EVAL(41U, (int32_T)c3_temp) != 0);
    if (c3_b_out) {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 41U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 4U,
                   chartInstance->c3_sfEvent);
      c3_c_out = (CV_TRANSITION_EVAL(4U, (int32_T)_SFD_CCP_CALL(5U, 4U, 0,
        (boolean_T)CV_RELATIONAL_EVAL(5U, 4U, 0, (real_T)
        chartInstance->c3_c_fails, 5.0, 0, 5U, chartInstance->c3_c_fails >= 5)
        != 0U, chartInstance->c3_sfEvent)) != 0);
      if (c3_c_out) {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
        c3_c_exit_internal_L1(chartInstance);
        chartInstance->c3_c_tp_L1 = 0U;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 3U, chartInstance->c3_sfEvent);
        chartInstance->c3_is_LI = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 2U, chartInstance->c3_sfEvent);
        chartInstance->c3_c_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
      } else {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 40U, chartInstance->c3_sfEvent);
        c3_c_exit_internal_L1(chartInstance);
        _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 40U,
                     chartInstance->c3_sfEvent);
        c3_b_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_LO == 0U) {
        } else {
          c3_LO(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_b_previousEvent;
        if (*chartInstance->c3_LI_mode == Isolated) {
          if (chartInstance->c3_is_LI != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 40U, chartInstance->c3_sfEvent);
          } else {
            c3_d_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_E;
            _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                         chartInstance->c3_sfEvent);
            if (chartInstance->c3_is_active_RO == 0U) {
            } else {
              c3_RO(chartInstance);
            }

            _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_sfEvent = c3_d_previousEvent;
            if (*chartInstance->c3_LI_mode == Isolated) {
              if (chartInstance->c3_is_LI != c3_IN_L1) {
                _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 40U,
                             chartInstance->c3_sfEvent);
              }
            } else {
              _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 40U,
                           chartInstance->c3_sfEvent);
            }
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 40U, chartInstance->c3_sfEvent);
        }

        if (*chartInstance->c3_LI_mode == Isolated) {
          if (chartInstance->c3_is_LI != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 40U, chartInstance->c3_sfEvent);
          } else {
            *chartInstance->c3_LI_mode = Off;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 5U, chartInstance->c3_sfEvent);
            chartInstance->c3_c_tp_Off = 1U;
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 40U, chartInstance->c3_sfEvent);
        }
      }
    } else {
      switch (*chartInstance->c3_LI_mode) {
       case Passive:
        CV_STATE_EVAL(3, 0, 3);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 43U,
                     chartInstance->c3_sfEvent);
        c3_d14 = c3_LO_act(chartInstance);
        c3_e_out = (CV_TRANSITION_EVAL(43U, (int32_T)_SFD_CCP_CALL(5U, 43U, 0,
          (c3_d14 != 0.0) != 0U, chartInstance->c3_sfEvent)) != 0);
        if (c3_e_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 43U, chartInstance->c3_sfEvent);
          chartInstance->c3_c_tp_Passive = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LI_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 7U, chartInstance->c3_sfEvent);
          chartInstance->c3_c_tp_Standby = 1U;
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 6U, chartInstance->c3_sfEvent);
        } else {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 46U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 45U,
                       chartInstance->c3_sfEvent);
          c3_d19 = c3_LO_act(chartInstance);
          c3_d_temp = !_SFD_CCP_CALL(5U, 45U, 0, (c3_d19 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
          if (!c3_d_temp) {
            c3_d20 = c3_RI_act(chartInstance);
            c3_d_temp = _SFD_CCP_CALL(5U, 45U, 1, (c3_d20 != 0.0) != 0U,
              chartInstance->c3_sfEvent);
          }

          c3_h_out = (CV_TRANSITION_EVAL(45U, (int32_T)c3_d_temp) != 0);
          if (c3_h_out) {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 45U, chartInstance->c3_sfEvent);
            chartInstance->c3_c_tp_Passive = 0U;
            _SFD_CS_CALL(STATE_INACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
            *chartInstance->c3_LI_mode = Active;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
            chartInstance->c3_c_tp_Active = 1U;
            c3_enter_atomic_Active(chartInstance);
            if (*chartInstance->c3_LI_mode != Active) {
            } else {
              _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 6U,
                           chartInstance->c3_sfEvent);
            }
          } else {
            _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 6U,
                         chartInstance->c3_sfEvent);
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 6U, chartInstance->c3_sfEvent);
          }
        }

        if (chartInstance->c3_is_LI != c3_IN_L1) {
        } else {
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
        }
        break;

       case Standby:
        CV_STATE_EVAL(3, 0, 4);
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 44U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 45U,
                     chartInstance->c3_sfEvent);
        c3_d16 = c3_LO_act(chartInstance);
        c3_c_temp = !_SFD_CCP_CALL(5U, 45U, 0, (c3_d16 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (!c3_c_temp) {
          c3_d18 = c3_RI_act(chartInstance);
          c3_c_temp = _SFD_CCP_CALL(5U, 45U, 1, (c3_d18 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_g_out = (CV_TRANSITION_EVAL(45U, (int32_T)c3_c_temp) != 0);
        if (c3_g_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 45U, chartInstance->c3_sfEvent);
          chartInstance->c3_c_tp_Standby = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 7U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LI_mode = Active;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
          chartInstance->c3_c_tp_Active = 1U;
          c3_enter_atomic_Active(chartInstance);
          if (*chartInstance->c3_LI_mode != Active) {
          } else {
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 7U, chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 7U,
                       chartInstance->c3_sfEvent);
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 7U, chartInstance->c3_sfEvent);
        }

        if (chartInstance->c3_is_LI != c3_IN_L1) {
        } else {
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
        }
        break;

       case Active:
        CV_STATE_EVAL(3, 0, 1);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 42U,
                     chartInstance->c3_sfEvent);
        c3_d15 = c3_RO_act(chartInstance);
        c3_b_temp = _SFD_CCP_CALL(5U, 42U, 0, (c3_d15 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (c3_b_temp) {
          c3_d17 = c3_LO_act(chartInstance);
          c3_b_temp = _SFD_CCP_CALL(5U, 42U, 1, (c3_d17 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_f_out = (CV_TRANSITION_EVAL(42U, (int32_T)c3_b_temp) != 0);
        if (c3_f_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 42U, chartInstance->c3_sfEvent);
          chartInstance->c3_c_tp_Active = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LI_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 7U, chartInstance->c3_sfEvent);
          chartInstance->c3_c_tp_Standby = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 4U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 4U, chartInstance->c3_sfEvent);
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
        break;

       case Off:
        CV_STATE_EVAL(3, 0, 2);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 39U,
                     chartInstance->c3_sfEvent);
        c3_d_out = (CV_TRANSITION_EVAL(39U, !_SFD_CCP_CALL(5U, 39U, 0,
          ((boolean_T *)&((char_T *)chartInstance->c3_u)[72])[1] != 0U,
          chartInstance->c3_sfEvent)) != 0);
        if (c3_d_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 39U, chartInstance->c3_sfEvent);
          if (*chartInstance->c3_LI_mode != Off) {
          } else {
            chartInstance->c3_c_tp_Off = 0U;
            _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 5U,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_c_fails = c3__s32_add__(chartInstance,
              chartInstance->c3_c_fails, 1, 27U, 7, 7);
            _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_c_fails, 2U);
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 5U, chartInstance->c3_sfEvent);
            *chartInstance->c3_LI_mode = Isolated;
            _SFD_CS_CALL(STATE_INACTIVE_TAG, 5U, chartInstance->c3_sfEvent);
          }

          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 1U, chartInstance->c3_sfEvent);
          *chartInstance->c3_LI_mode = Passive;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
          chartInstance->c3_c_tp_Passive = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 5U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 5U, chartInstance->c3_sfEvent);
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
        break;

       default:
        CV_STATE_EVAL(3, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_LI_mode = Isolated;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 3U, chartInstance->c3_sfEvent);
        break;
      }
    }
  }
}

static void c3_c_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  switch (*chartInstance->c3_LI_mode) {
   case Active:
    CV_STATE_EVAL(3, 1, 1);
    chartInstance->c3_c_tp_Active = 0U;
    *chartInstance->c3_LI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
    break;

   case Off:
    CV_STATE_EVAL(3, 1, 2);
    chartInstance->c3_c_tp_Off = 0U;
    _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 5U, chartInstance->c3_sfEvent);
    chartInstance->c3_c_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_c_fails, 1, 27U, 7, 7);
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_c_fails, 2U);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 5U, chartInstance->c3_sfEvent);
    *chartInstance->c3_LI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 5U, chartInstance->c3_sfEvent);
    break;

   case Passive:
    CV_STATE_EVAL(3, 1, 3);
    chartInstance->c3_c_tp_Passive = 0U;
    *chartInstance->c3_LI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 6U, chartInstance->c3_sfEvent);
    break;

   case Standby:
    CV_STATE_EVAL(3, 1, 4);
    chartInstance->c3_c_tp_Standby = 0U;
    *chartInstance->c3_LI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 7U, chartInstance->c3_sfEvent);
    break;

   default:
    CV_STATE_EVAL(3, 1, 0);
    *chartInstance->c3_LI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 4U, chartInstance->c3_sfEvent);
    break;
  }
}

static void c3_enter_atomic_Active(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  int32_T c3_previousEvent;
  c3_previousEvent = chartInstance->c3_sfEvent;
  chartInstance->c3_sfEvent = c3_event_E;
  _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E, chartInstance->c3_sfEvent);
  if (chartInstance->c3_is_active_LO == 0U) {
  } else {
    c3_LO(chartInstance);
  }

  _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E, chartInstance->c3_sfEvent);
  chartInstance->c3_sfEvent = c3_previousEvent;
}

static void c3_RI(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  _SF_MEX_LISTEN_FOR_CTRL_C(chartInstance->S);
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 15U, chartInstance->c3_sfEvent);
  switch (chartInstance->c3_is_RI) {
   case c3_IN_Isolated:
    CV_STATE_EVAL(15, 0, c3_IN_Isolated);
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 16U, chartInstance->c3_sfEvent);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 16U, chartInstance->c3_sfEvent);
    break;

   case c3_IN_L1:
    CV_STATE_EVAL(15, 0, c3_IN_L1);
    c3_d_L1(chartInstance);
    break;

   default:
    CV_STATE_EVAL(15, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_RI = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 16U, chartInstance->c3_sfEvent);
    break;
  }

  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 15U, chartInstance->c3_sfEvent);
}

static void c3_d_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  real_T c3_d21;
  real_T c3_d22;
  boolean_T c3_d_out;
  real_T c3_d23;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  real_T c3_d24;
  real_T c3_d25;
  boolean_T c3_e_out;
  int32_T c3_b_previousEvent;
  real_T c3_d26;
  boolean_T c3_f_out;
  int32_T c3_c_previousEvent;
  boolean_T c3_d_temp;
  real_T c3_d27;
  boolean_T c3_g_out;
  int32_T c3_d_previousEvent;
  int32_T c3_e_previousEvent;
  int32_T c3_f_previousEvent;
  _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 36U, chartInstance->c3_sfEvent);
  c3_out = (CV_TRANSITION_EVAL(36U, (int32_T)_SFD_CCP_CALL(5U, 36U, 0,
              (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U,
              chartInstance->c3_sfEvent)) != 0);
  if (c3_out) {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 36U, chartInstance->c3_sfEvent);
    c3_d_exit_internal_L1(chartInstance);
    chartInstance->c3_d_tp_L1 = 0U;
    chartInstance->c3_is_RI = c3_IN_NO_ACTIVE_CHILD;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 17U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 36U,
                 chartInstance->c3_sfEvent);
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    if (chartInstance->c3_is_active_RO == 0U) {
    } else {
      c3_RO(chartInstance);
    }

    _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                 chartInstance->c3_sfEvent);
    chartInstance->c3_sfEvent = c3_previousEvent;
    if (chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_RI == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U, chartInstance->c3_sfEvent);
      } else {
        c3_c_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_LO == 0U) {
        } else {
          c3_LO(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_c_previousEvent;
        if (chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) {
          if (chartInstance->c3_is_active_RI == 0U) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U, chartInstance->c3_sfEvent);
          } else {
            c3_e_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_E;
            _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                         chartInstance->c3_sfEvent);
            if (chartInstance->c3_is_active_LI == 0U) {
            } else {
              c3_LI(chartInstance);
            }

            _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_sfEvent = c3_e_previousEvent;
            if (chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) {
              if (chartInstance->c3_is_active_RI == 0U) {
                _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U,
                             chartInstance->c3_sfEvent);
              }
            } else {
              _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U,
                           chartInstance->c3_sfEvent);
            }
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U, chartInstance->c3_sfEvent);
        }
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U, chartInstance->c3_sfEvent);
    }

    if (chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) {
      if (chartInstance->c3_is_active_RI == 0U) {
        _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U, chartInstance->c3_sfEvent);
      } else {
        chartInstance->c3_is_RI = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 16U, chartInstance->c3_sfEvent);
        chartInstance->c3_d_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
      }
    } else {
      _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 36U, chartInstance->c3_sfEvent);
    }
  } else {
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 25U,
                 chartInstance->c3_sfEvent);
    c3_temp = _SFD_CCP_CALL(5U, 25U, 0, (chartInstance->c3_sfEvent ==
      c3_event_go_off) != 0U, chartInstance->c3_sfEvent);
    if (c3_temp) {
      c3_temp = !_SFD_CCP_CALL(5U, 25U, 1, (*chartInstance->c3_RI_mode == Off)
        != 0U, chartInstance->c3_sfEvent);
    }

    c3_b_out = (CV_TRANSITION_EVAL(25U, (int32_T)c3_temp) != 0);
    if (c3_b_out) {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 25U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 37U,
                   chartInstance->c3_sfEvent);
      c3_c_out = (CV_TRANSITION_EVAL(37U, (int32_T)_SFD_CCP_CALL(5U, 37U, 0,
        (boolean_T)CV_RELATIONAL_EVAL(5U, 37U, 0, (real_T)
        chartInstance->c3_d_fails, 5.0, 0, 5U, chartInstance->c3_d_fails >= 5)
        != 0U, chartInstance->c3_sfEvent)) != 0);
      if (c3_c_out) {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 37U, chartInstance->c3_sfEvent);
        c3_d_exit_internal_L1(chartInstance);
        chartInstance->c3_d_tp_L1 = 0U;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 17U, chartInstance->c3_sfEvent);
        chartInstance->c3_is_RI = c3_IN_Isolated;
        _SFD_CS_CALL(STATE_ACTIVE_TAG, 16U, chartInstance->c3_sfEvent);
        chartInstance->c3_d_tp_Isolated = 1U;
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
      } else {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
        c3_d_exit_internal_L1(chartInstance);
        _SFD_CT_CALL(TRANSITION_BEFORE_TRANS_ACTION_TAG, 13U,
                     chartInstance->c3_sfEvent);
        c3_b_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_RO == 0U) {
        } else {
          c3_RO(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_b_previousEvent;
        if (*chartInstance->c3_RI_mode == Isolated) {
          if (chartInstance->c3_is_RI != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
          } else {
            c3_d_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_E;
            _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                         chartInstance->c3_sfEvent);
            if (chartInstance->c3_is_active_LO == 0U) {
            } else {
              c3_LO(chartInstance);
            }

            _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_sfEvent = c3_d_previousEvent;
            if (*chartInstance->c3_RI_mode == Isolated) {
              if (chartInstance->c3_is_RI != c3_IN_L1) {
                _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U,
                             chartInstance->c3_sfEvent);
              } else {
                c3_f_previousEvent = chartInstance->c3_sfEvent;
                chartInstance->c3_sfEvent = c3_event_E;
                _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E,
                             chartInstance->c3_sfEvent);
                if (chartInstance->c3_is_active_LI == 0U) {
                } else {
                  c3_LI(chartInstance);
                }

                _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E,
                             chartInstance->c3_sfEvent);
                chartInstance->c3_sfEvent = c3_f_previousEvent;
                if (*chartInstance->c3_RI_mode == Isolated) {
                  if (chartInstance->c3_is_RI != c3_IN_L1) {
                    _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U,
                                 chartInstance->c3_sfEvent);
                  }
                } else {
                  _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U,
                               chartInstance->c3_sfEvent);
                }
              }
            } else {
              _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U,
                           chartInstance->c3_sfEvent);
            }
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
        }

        if (*chartInstance->c3_RI_mode == Isolated) {
          if (chartInstance->c3_is_RI != c3_IN_L1) {
            _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
          } else {
            *chartInstance->c3_RI_mode = Off;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 19U, chartInstance->c3_sfEvent);
            chartInstance->c3_d_tp_Off = 1U;
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U,
                         chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CT_CALL(TRANSITION_INACTIVE_TAG, 13U, chartInstance->c3_sfEvent);
        }
      }
    } else {
      switch (*chartInstance->c3_RI_mode) {
       case Passive:
        CV_STATE_EVAL(17, 0, 3);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 29U,
                     chartInstance->c3_sfEvent);
        c3_d21 = c3_RO_act(chartInstance);
        c3_d_out = (CV_TRANSITION_EVAL(29U, (int32_T)_SFD_CCP_CALL(5U, 29U, 0,
          (c3_d21 != 0.0) != 0U, chartInstance->c3_sfEvent)) != 0);
        if (c3_d_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 29U, chartInstance->c3_sfEvent);
          chartInstance->c3_d_tp_Passive = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
          *chartInstance->c3_RI_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 21U, chartInstance->c3_sfEvent);
          chartInstance->c3_d_tp_Standby = 1U;
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 20U, chartInstance->c3_sfEvent);
        } else {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 34U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 33U,
                       chartInstance->c3_sfEvent);
          c3_d26 = c3_RO_act(chartInstance);
          c3_d_temp = !_SFD_CCP_CALL(5U, 33U, 0, (c3_d26 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
          if (!c3_d_temp) {
            c3_d27 = c3_LI_act(chartInstance);
            c3_d_temp = _SFD_CCP_CALL(5U, 33U, 1, (c3_d27 != 0.0) != 0U,
              chartInstance->c3_sfEvent);
          }

          c3_g_out = (CV_TRANSITION_EVAL(33U, (int32_T)c3_d_temp) != 0);
          if (c3_g_out) {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 33U, chartInstance->c3_sfEvent);
            chartInstance->c3_d_tp_Passive = 0U;
            _SFD_CS_CALL(STATE_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
            *chartInstance->c3_RI_mode = Active;
            _SFD_CS_CALL(STATE_ACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
            chartInstance->c3_d_tp_Active = 1U;
            c3_b_enter_atomic_Active(chartInstance);
            if (*chartInstance->c3_RI_mode != Active) {
            } else {
              _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 20U,
                           chartInstance->c3_sfEvent);
            }
          } else {
            _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 20U,
                         chartInstance->c3_sfEvent);
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 20U,
                         chartInstance->c3_sfEvent);
          }
        }

        if (chartInstance->c3_is_RI != c3_IN_L1) {
        } else {
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
        }
        break;

       case Standby:
        CV_STATE_EVAL(17, 0, 4);
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 32U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 33U,
                     chartInstance->c3_sfEvent);
        c3_d23 = c3_RO_act(chartInstance);
        c3_c_temp = !_SFD_CCP_CALL(5U, 33U, 0, (c3_d23 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (!c3_c_temp) {
          c3_d25 = c3_LI_act(chartInstance);
          c3_c_temp = _SFD_CCP_CALL(5U, 33U, 1, (c3_d25 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_f_out = (CV_TRANSITION_EVAL(33U, (int32_T)c3_c_temp) != 0);
        if (c3_f_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 33U, chartInstance->c3_sfEvent);
          chartInstance->c3_d_tp_Standby = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 21U, chartInstance->c3_sfEvent);
          *chartInstance->c3_RI_mode = Active;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
          chartInstance->c3_d_tp_Active = 1U;
          c3_b_enter_atomic_Active(chartInstance);
          if (*chartInstance->c3_RI_mode != Active) {
          } else {
            _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 21U,
                         chartInstance->c3_sfEvent);
          }
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 21U,
                       chartInstance->c3_sfEvent);
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 21U, chartInstance->c3_sfEvent);
        }

        if (chartInstance->c3_is_RI != c3_IN_L1) {
        } else {
          _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
        }
        break;

       case Active:
        CV_STATE_EVAL(17, 0, 1);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 26U,
                     chartInstance->c3_sfEvent);
        c3_d22 = c3_LO_act(chartInstance);
        c3_b_temp = _SFD_CCP_CALL(5U, 26U, 0, (c3_d22 != 0.0) != 0U,
          chartInstance->c3_sfEvent);
        if (c3_b_temp) {
          c3_d24 = c3_RO_act(chartInstance);
          c3_b_temp = _SFD_CCP_CALL(5U, 26U, 1, (c3_d24 != 0.0) != 0U,
            chartInstance->c3_sfEvent);
        }

        c3_e_out = (CV_TRANSITION_EVAL(26U, (int32_T)c3_b_temp) != 0);
        if (c3_e_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 26U, chartInstance->c3_sfEvent);
          chartInstance->c3_d_tp_Active = 0U;
          _SFD_CS_CALL(STATE_INACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
          *chartInstance->c3_RI_mode = Standby;
          _SFD_CS_CALL(STATE_ACTIVE_TAG, 21U, chartInstance->c3_sfEvent);
          chartInstance->c3_d_tp_Standby = 1U;
        } else {
          _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 18U,
                       chartInstance->c3_sfEvent);
        }

        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 18U, chartInstance->c3_sfEvent);
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
        break;

       case Off:
        CV_STATE_EVAL(17, 0, 2);
        c3_Off(chartInstance);
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
        break;

       default:
        CV_STATE_EVAL(17, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_RI_mode = Isolated;
        _SFD_CS_CALL(STATE_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
        _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 17U, chartInstance->c3_sfEvent);
        break;
      }
    }
  }
}

static void c3_d_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  switch (*chartInstance->c3_RI_mode) {
   case Active:
    CV_STATE_EVAL(17, 1, 1);
    chartInstance->c3_d_tp_Active = 0U;
    *chartInstance->c3_RI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
    break;

   case Off:
    CV_STATE_EVAL(17, 1, 2);
    chartInstance->c3_d_tp_Off = 0U;
    _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 19U, chartInstance->c3_sfEvent);
    chartInstance->c3_d_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_d_fails, 1, 34U, 7, 7);
    _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_d_fails, 3U);
    _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 19U, chartInstance->c3_sfEvent);
    *chartInstance->c3_RI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 19U, chartInstance->c3_sfEvent);
    break;

   case Passive:
    CV_STATE_EVAL(17, 1, 3);
    chartInstance->c3_d_tp_Passive = 0U;
    *chartInstance->c3_RI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
    break;

   case Standby:
    CV_STATE_EVAL(17, 1, 4);
    chartInstance->c3_d_tp_Standby = 0U;
    *chartInstance->c3_RI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 21U, chartInstance->c3_sfEvent);
    break;

   default:
    CV_STATE_EVAL(17, 1, 0);
    *chartInstance->c3_RI_mode = Isolated;
    _SFD_CS_CALL(STATE_INACTIVE_TAG, 18U, chartInstance->c3_sfEvent);
    break;
  }
}

static void c3_b_enter_atomic_Active(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  int32_T c3_previousEvent;
  c3_previousEvent = chartInstance->c3_sfEvent;
  chartInstance->c3_sfEvent = c3_event_E;
  _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_E, chartInstance->c3_sfEvent);
  if (chartInstance->c3_is_active_RO == 0U) {
  } else {
    c3_RO(chartInstance);
  }

  _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_E, chartInstance->c3_sfEvent);
  chartInstance->c3_sfEvent = c3_previousEvent;
}

static void c3_Off(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 8U, chartInstance->c3_sfEvent);
  c3_out = (CV_TRANSITION_EVAL(8U, !_SFD_CCP_CALL(5U, 8U, 0, ((boolean_T *)
    &((char_T *)chartInstance->c3_u)[72])[1] != 0U, chartInstance->c3_sfEvent))
            != 0);
  if (c3_out) {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 8U, chartInstance->c3_sfEvent);
    if (*chartInstance->c3_RI_mode != Off) {
    } else {
      chartInstance->c3_d_tp_Off = 0U;
      _SFD_CS_CALL(STATE_ENTER_EXIT_FUNCTION_TAG, 19U, chartInstance->c3_sfEvent);
      chartInstance->c3_d_fails = c3__s32_add__(chartInstance,
        chartInstance->c3_d_fails, 1, 34U, 7, 7);
      _SFD_DATA_RANGE_CHECK((real_T)chartInstance->c3_d_fails, 3U);
      _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 19U, chartInstance->c3_sfEvent);
      *chartInstance->c3_RI_mode = Isolated;
      _SFD_CS_CALL(STATE_INACTIVE_TAG, 19U, chartInstance->c3_sfEvent);
    }

    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 35U, chartInstance->c3_sfEvent);
    *chartInstance->c3_RI_mode = Passive;
    _SFD_CS_CALL(STATE_ACTIVE_TAG, 20U, chartInstance->c3_sfEvent);
    chartInstance->c3_d_tp_Passive = 1U;
  } else {
    _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 19U, chartInstance->c3_sfEvent);
  }

  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 19U, chartInstance->c3_sfEvent);
}

static void init_script_number_translation(uint32_T c3_machineNumber, uint32_T
  c3_chartNumber, uint32_T c3_instanceNumber)
{
  (void)(c3_machineNumber);
  (void)(c3_chartNumber);
  (void)(c3_instanceNumber);
}

const mxArray *sf_c3_sf_aircraft_fault_get_eml_resolved_functions_info(void)
{
  const mxArray *c3_nameCaptureInfo = NULL;
  c3_nameCaptureInfo = NULL;
  sf_mex_assign(&c3_nameCaptureInfo, sf_mex_create("nameCaptureInfo", NULL, 0,
    0U, 1U, 0U, 2, 0, 1), false);
  return c3_nameCaptureInfo;
}

static void c3_L_switch(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_aVarTruthTableCondition_4;
  boolean_T c3_aVarTruthTableCondition_3;
  boolean_T c3_aVarTruthTableCondition_2;
  boolean_T c3_aVarTruthTableCondition_1;
  boolean_T c3_temp;
  boolean_T c3_b_temp;
  boolean_T c3_out;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_temp;
  int32_T c3_b_previousEvent;
  boolean_T c3_d_temp;
  boolean_T c3_e_temp;
  int32_T c3_c_previousEvent;
  boolean_T c3_c_out;
  boolean_T c3_f_temp;
  int32_T c3_d_previousEvent;
  boolean_T c3_d_out;
  boolean_T c3_e_out;
  int32_T c3_e_previousEvent;
  boolean_T c3_f_out;
  int32_T c3_f_previousEvent;
  int32_T c3_g_previousEvent;
  int32_T c3_h_previousEvent;
  _SFD_SET_DATA_VALUE_PTR(12U, (void *)&c3_aVarTruthTableCondition_4);
  _SFD_SET_DATA_VALUE_PTR(11U, (void *)&c3_aVarTruthTableCondition_3);
  _SFD_SET_DATA_VALUE_PTR(10U, (void *)&c3_aVarTruthTableCondition_2);
  _SFD_SET_DATA_VALUE_PTR(9U, (void *)&c3_aVarTruthTableCondition_1);
  _SFD_CS_CALL(FUNCTION_ACTIVE_TAG, 31U, chartInstance->c3_sfEvent);
  _SFD_SYMBOL_SCOPE_PUSH(4U, 0U);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_1",
    &c3_aVarTruthTableCondition_1, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_2",
    &c3_aVarTruthTableCondition_2, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_3",
    &c3_aVarTruthTableCondition_3, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_4",
    &c3_aVarTruthTableCondition_4, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 31U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_1 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_1, 9U);
  c3_aVarTruthTableCondition_2 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_2, 10U);
  c3_aVarTruthTableCondition_3 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_3, 11U);
  c3_aVarTruthTableCondition_4 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_4, 12U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 52U, chartInstance->c3_sfEvent);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 53U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_1 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[0];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_1, 9U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 54U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_2 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [16])[0];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_2, 10U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 55U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_3 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[1];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_3, 11U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 56U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_4 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [16])[1];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_4, 12U);
  _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 57U, chartInstance->c3_sfEvent);
  c3_temp = _SFD_CCP_CALL(5U, 57U, 0, c3_aVarTruthTableCondition_1 != 0U,
    chartInstance->c3_sfEvent);
  if (c3_temp) {
    c3_temp = !_SFD_CCP_CALL(5U, 57U, 1, c3_aVarTruthTableCondition_3 != 0U,
      chartInstance->c3_sfEvent);
  }

  c3_b_temp = c3_temp;
  if (c3_b_temp) {
    c3_b_temp = !_SFD_CCP_CALL(5U, 57U, 2, c3_aVarTruthTableCondition_4 != 0U,
      chartInstance->c3_sfEvent);
  }

  c3_out = (CV_TRANSITION_EVAL(57U, (int32_T)c3_b_temp) != 0);
  if (c3_out) {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 57U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 58U, chartInstance->c3_sfEvent);
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_go_off;
    _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_off,
                 chartInstance->c3_sfEvent);
    if (chartInstance->c3_is_active_LO == 0U) {
    } else {
      c3_LO(chartInstance);
    }

    _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_off,
                 chartInstance->c3_sfEvent);
    chartInstance->c3_sfEvent = c3_previousEvent;
  } else {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 59U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 60U,
                 chartInstance->c3_sfEvent);
    c3_b_out = (CV_TRANSITION_EVAL(60U, (int32_T)_SFD_CCP_CALL(5U, 60U, 0,
      c3_aVarTruthTableCondition_1 != 0U, chartInstance->c3_sfEvent)) != 0);
    if (c3_b_out) {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 60U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 61U, chartInstance->c3_sfEvent);
      c3_b_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      if (chartInstance->c3_is_active_LO == 0U) {
      } else {
        c3_LO(chartInstance);
      }

      _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      chartInstance->c3_sfEvent = c3_b_previousEvent;
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 62U, chartInstance->c3_sfEvent);
      c3_c_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      if (chartInstance->c3_is_active_LI == 0U) {
      } else {
        c3_LI(chartInstance);
      }

      _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      chartInstance->c3_sfEvent = c3_c_previousEvent;
    } else {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 63U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 64U,
                   chartInstance->c3_sfEvent);
      c3_c_temp = !_SFD_CCP_CALL(5U, 64U, 0, c3_aVarTruthTableCondition_1 != 0U,
        chartInstance->c3_sfEvent);
      if (c3_c_temp) {
        c3_c_temp = _SFD_CCP_CALL(5U, 64U, 1, c3_aVarTruthTableCondition_2 != 0U,
          chartInstance->c3_sfEvent);
      }

      c3_d_temp = c3_c_temp;
      if (c3_d_temp) {
        c3_d_temp = !_SFD_CCP_CALL(5U, 64U, 2, c3_aVarTruthTableCondition_3 !=
          0U, chartInstance->c3_sfEvent);
      }

      c3_e_temp = c3_d_temp;
      if (c3_e_temp) {
        c3_e_temp = !_SFD_CCP_CALL(5U, 64U, 3, c3_aVarTruthTableCondition_4 !=
          0U, chartInstance->c3_sfEvent);
      }

      c3_c_out = (CV_TRANSITION_EVAL(64U, (int32_T)c3_e_temp) != 0);
      if (c3_c_out) {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 64U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 65U, chartInstance->c3_sfEvent);
        c3_d_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_go_isolated;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_LO == 0U) {
        } else {
          c3_LO(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_d_previousEvent;
      } else {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 66U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 67U,
                     chartInstance->c3_sfEvent);
        c3_f_temp = !_SFD_CCP_CALL(5U, 67U, 0, c3_aVarTruthTableCondition_1 !=
          0U, chartInstance->c3_sfEvent);
        if (c3_f_temp) {
          c3_f_temp = _SFD_CCP_CALL(5U, 67U, 1, c3_aVarTruthTableCondition_2 !=
            0U, chartInstance->c3_sfEvent);
        }

        c3_d_out = (CV_TRANSITION_EVAL(67U, (int32_T)c3_f_temp) != 0);
        if (c3_d_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 67U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 68U, chartInstance->c3_sfEvent);
          c3_e_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          if (chartInstance->c3_is_active_LO == 0U) {
          } else {
            c3_LO(chartInstance);
          }

          _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          chartInstance->c3_sfEvent = c3_e_previousEvent;
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 69U, chartInstance->c3_sfEvent);
          c3_h_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          if (chartInstance->c3_is_active_LI == 0U) {
          } else {
            c3_LI(chartInstance);
          }

          _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          chartInstance->c3_sfEvent = c3_h_previousEvent;
        } else {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 70U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 71U,
                       chartInstance->c3_sfEvent);
          c3_e_out = (CV_TRANSITION_EVAL(71U, (int32_T)_SFD_CCP_CALL(5U, 71U, 0,
            c3_aVarTruthTableCondition_3 != 0U, chartInstance->c3_sfEvent)) != 0);
          if (c3_e_out) {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 71U, chartInstance->c3_sfEvent);
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 72U, chartInstance->c3_sfEvent);
            c3_f_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_go_off;
            _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_off,
                         chartInstance->c3_sfEvent);
            if (chartInstance->c3_is_active_LI == 0U) {
            } else {
              c3_LI(chartInstance);
            }

            _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_off,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_sfEvent = c3_f_previousEvent;
          } else {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 73U, chartInstance->c3_sfEvent);
            _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 74U,
                         chartInstance->c3_sfEvent);
            c3_f_out = (CV_TRANSITION_EVAL(74U, (int32_T)_SFD_CCP_CALL(5U, 74U,
              0, c3_aVarTruthTableCondition_4 != 0U, chartInstance->c3_sfEvent))
                        != 0);
            if (c3_f_out) {
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 74U, chartInstance->c3_sfEvent);
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 75U, chartInstance->c3_sfEvent);
              c3_g_previousEvent = chartInstance->c3_sfEvent;
              chartInstance->c3_sfEvent = c3_event_go_isolated;
              _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                           chartInstance->c3_sfEvent);
              if (chartInstance->c3_is_active_LI == 0U) {
              } else {
                c3_LI(chartInstance);
              }

              _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                           chartInstance->c3_sfEvent);
              chartInstance->c3_sfEvent = c3_g_previousEvent;
            } else {
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 76U, chartInstance->c3_sfEvent);
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 77U, chartInstance->c3_sfEvent);
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 78U, chartInstance->c3_sfEvent);
            }
          }
        }
      }
    }
  }

  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CS_CALL(FUNCTION_INACTIVE_TAG, 31U, chartInstance->c3_sfEvent);
  _SFD_UNSET_DATA_VALUE_PTR(12U);
  _SFD_UNSET_DATA_VALUE_PTR(11U);
  _SFD_UNSET_DATA_VALUE_PTR(10U);
  _SFD_UNSET_DATA_VALUE_PTR(9U);
  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 31U, chartInstance->c3_sfEvent);
}

static void c3_R_switch(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_aVarTruthTableCondition_4;
  boolean_T c3_aVarTruthTableCondition_3;
  boolean_T c3_aVarTruthTableCondition_2;
  boolean_T c3_aVarTruthTableCondition_1;
  boolean_T c3_temp;
  boolean_T c3_b_temp;
  boolean_T c3_out;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_temp;
  int32_T c3_b_previousEvent;
  boolean_T c3_d_temp;
  boolean_T c3_e_temp;
  int32_T c3_c_previousEvent;
  boolean_T c3_c_out;
  boolean_T c3_f_temp;
  int32_T c3_d_previousEvent;
  boolean_T c3_d_out;
  boolean_T c3_e_out;
  int32_T c3_e_previousEvent;
  boolean_T c3_f_out;
  int32_T c3_f_previousEvent;
  int32_T c3_g_previousEvent;
  int32_T c3_h_previousEvent;
  _SFD_SET_DATA_VALUE_PTR(16U, (void *)&c3_aVarTruthTableCondition_4);
  _SFD_SET_DATA_VALUE_PTR(15U, (void *)&c3_aVarTruthTableCondition_3);
  _SFD_SET_DATA_VALUE_PTR(14U, (void *)&c3_aVarTruthTableCondition_2);
  _SFD_SET_DATA_VALUE_PTR(13U, (void *)&c3_aVarTruthTableCondition_1);
  _SFD_CS_CALL(FUNCTION_ACTIVE_TAG, 34U, chartInstance->c3_sfEvent);
  _SFD_SYMBOL_SCOPE_PUSH(4U, 0U);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_1",
    &c3_aVarTruthTableCondition_1, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_2",
    &c3_aVarTruthTableCondition_2, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_3",
    &c3_aVarTruthTableCondition_3, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("aVarTruthTableCondition_4",
    &c3_aVarTruthTableCondition_4, c3_e_sf_marshallOut, c3_d_sf_marshallIn);
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 34U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_1 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_1, 13U);
  c3_aVarTruthTableCondition_2 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_2, 14U);
  c3_aVarTruthTableCondition_3 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_3, 15U);
  c3_aVarTruthTableCondition_4 = false;
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_4, 16U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 79U, chartInstance->c3_sfEvent);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 80U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_1 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[2];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_1, 13U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 81U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_2 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [40])[0];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_2, 14U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 82U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_3 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[1];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_3, 15U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 83U, chartInstance->c3_sfEvent);
  c3_aVarTruthTableCondition_4 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [40])[1];
  _SFD_DATA_RANGE_CHECK((real_T)c3_aVarTruthTableCondition_4, 16U);
  _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 84U, chartInstance->c3_sfEvent);
  c3_temp = _SFD_CCP_CALL(5U, 84U, 0, c3_aVarTruthTableCondition_1 != 0U,
    chartInstance->c3_sfEvent);
  if (c3_temp) {
    c3_temp = !_SFD_CCP_CALL(5U, 84U, 1, c3_aVarTruthTableCondition_3 != 0U,
      chartInstance->c3_sfEvent);
  }

  c3_b_temp = c3_temp;
  if (c3_b_temp) {
    c3_b_temp = !_SFD_CCP_CALL(5U, 84U, 2, c3_aVarTruthTableCondition_4 != 0U,
      chartInstance->c3_sfEvent);
  }

  c3_out = (CV_TRANSITION_EVAL(84U, (int32_T)c3_b_temp) != 0);
  if (c3_out) {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 84U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 85U, chartInstance->c3_sfEvent);
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_go_off;
    _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_off,
                 chartInstance->c3_sfEvent);
    if (chartInstance->c3_is_active_RO == 0U) {
    } else {
      c3_RO(chartInstance);
    }

    _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_off,
                 chartInstance->c3_sfEvent);
    chartInstance->c3_sfEvent = c3_previousEvent;
  } else {
    _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 86U, chartInstance->c3_sfEvent);
    _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 87U,
                 chartInstance->c3_sfEvent);
    c3_b_out = (CV_TRANSITION_EVAL(87U, (int32_T)_SFD_CCP_CALL(5U, 87U, 0,
      c3_aVarTruthTableCondition_1 != 0U, chartInstance->c3_sfEvent)) != 0);
    if (c3_b_out) {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 87U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 88U, chartInstance->c3_sfEvent);
      c3_b_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      if (chartInstance->c3_is_active_RO == 0U) {
      } else {
        c3_RO(chartInstance);
      }

      _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      chartInstance->c3_sfEvent = c3_b_previousEvent;
      c3_c_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      if (chartInstance->c3_is_active_RI == 0U) {
      } else {
        c3_RI(chartInstance);
      }

      _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                   chartInstance->c3_sfEvent);
      chartInstance->c3_sfEvent = c3_c_previousEvent;
    } else {
      _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 89U, chartInstance->c3_sfEvent);
      _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 90U,
                   chartInstance->c3_sfEvent);
      c3_c_temp = !_SFD_CCP_CALL(5U, 90U, 0, c3_aVarTruthTableCondition_1 != 0U,
        chartInstance->c3_sfEvent);
      if (c3_c_temp) {
        c3_c_temp = _SFD_CCP_CALL(5U, 90U, 1, c3_aVarTruthTableCondition_2 != 0U,
          chartInstance->c3_sfEvent);
      }

      c3_d_temp = c3_c_temp;
      if (c3_d_temp) {
        c3_d_temp = !_SFD_CCP_CALL(5U, 90U, 2, c3_aVarTruthTableCondition_3 !=
          0U, chartInstance->c3_sfEvent);
      }

      c3_e_temp = c3_d_temp;
      if (c3_e_temp) {
        c3_e_temp = !_SFD_CCP_CALL(5U, 90U, 3, c3_aVarTruthTableCondition_4 !=
          0U, chartInstance->c3_sfEvent);
      }

      c3_c_out = (CV_TRANSITION_EVAL(90U, (int32_T)c3_e_temp) != 0);
      if (c3_c_out) {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 90U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 91U, chartInstance->c3_sfEvent);
        c3_d_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_go_isolated;
        _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                     chartInstance->c3_sfEvent);
        if (chartInstance->c3_is_active_RO == 0U) {
        } else {
          c3_RO(chartInstance);
        }

        _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                     chartInstance->c3_sfEvent);
        chartInstance->c3_sfEvent = c3_d_previousEvent;
      } else {
        _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 92U, chartInstance->c3_sfEvent);
        _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 93U,
                     chartInstance->c3_sfEvent);
        c3_f_temp = !_SFD_CCP_CALL(5U, 93U, 0, c3_aVarTruthTableCondition_1 !=
          0U, chartInstance->c3_sfEvent);
        if (c3_f_temp) {
          c3_f_temp = _SFD_CCP_CALL(5U, 93U, 1, c3_aVarTruthTableCondition_2 !=
            0U, chartInstance->c3_sfEvent);
        }

        c3_d_out = (CV_TRANSITION_EVAL(93U, (int32_T)c3_f_temp) != 0);
        if (c3_d_out) {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 93U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 94U, chartInstance->c3_sfEvent);
          c3_e_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          if (chartInstance->c3_is_active_RO == 0U) {
          } else {
            c3_RO(chartInstance);
          }

          _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          chartInstance->c3_sfEvent = c3_e_previousEvent;
          c3_g_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          if (chartInstance->c3_is_active_RI == 0U) {
          } else {
            c3_RI(chartInstance);
          }

          _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                       chartInstance->c3_sfEvent);
          chartInstance->c3_sfEvent = c3_g_previousEvent;
        } else {
          _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 95U, chartInstance->c3_sfEvent);
          _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 96U,
                       chartInstance->c3_sfEvent);
          c3_e_out = (CV_TRANSITION_EVAL(96U, (int32_T)_SFD_CCP_CALL(5U, 96U, 0,
            c3_aVarTruthTableCondition_3 != 0U, chartInstance->c3_sfEvent)) != 0);
          if (c3_e_out) {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 96U, chartInstance->c3_sfEvent);
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 97U, chartInstance->c3_sfEvent);
            c3_f_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_go_off;
            _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_off,
                         chartInstance->c3_sfEvent);
            if (chartInstance->c3_is_active_RI == 0U) {
            } else {
              c3_RI(chartInstance);
            }

            _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_off,
                         chartInstance->c3_sfEvent);
            chartInstance->c3_sfEvent = c3_f_previousEvent;
          } else {
            _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 98U, chartInstance->c3_sfEvent);
            _SFD_CT_CALL(TRANSITION_BEFORE_PROCESSING_TAG, 99U,
                         chartInstance->c3_sfEvent);
            c3_f_out = (CV_TRANSITION_EVAL(99U, (int32_T)_SFD_CCP_CALL(5U, 99U,
              0, c3_aVarTruthTableCondition_4 != 0U, chartInstance->c3_sfEvent))
                        != 0);
            if (c3_f_out) {
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 99U, chartInstance->c3_sfEvent);
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 100U,
                           chartInstance->c3_sfEvent);
              c3_h_previousEvent = chartInstance->c3_sfEvent;
              chartInstance->c3_sfEvent = c3_event_go_isolated;
              _SFD_CE_CALL(EVENT_BEFORE_BROADCAST_TAG, c3_event_go_isolated,
                           chartInstance->c3_sfEvent);
              if (chartInstance->c3_is_active_RI == 0U) {
              } else {
                c3_RI(chartInstance);
              }

              _SFD_CE_CALL(EVENT_AFTER_BROADCAST_TAG, c3_event_go_isolated,
                           chartInstance->c3_sfEvent);
              chartInstance->c3_sfEvent = c3_h_previousEvent;
            } else {
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 101U,
                           chartInstance->c3_sfEvent);
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 102U,
                           chartInstance->c3_sfEvent);
              _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 103U,
                           chartInstance->c3_sfEvent);
            }
          }
        }
      }
    }
  }

  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CS_CALL(FUNCTION_INACTIVE_TAG, 34U, chartInstance->c3_sfEvent);
  _SFD_UNSET_DATA_VALUE_PTR(16U);
  _SFD_UNSET_DATA_VALUE_PTR(15U);
  _SFD_UNSET_DATA_VALUE_PTR(14U);
  _SFD_UNSET_DATA_VALUE_PTR(13U);
  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 34U, chartInstance->c3_sfEvent);
}

static real_T c3_LO_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  real_T c3_y_act;
  _SFD_SET_DATA_VALUE_PTR(17U, (void *)&c3_y_act);
  _SFD_CS_CALL(FUNCTION_ACTIVE_TAG, 30U, chartInstance->c3_sfEvent);
  _SFD_SYMBOL_SCOPE_PUSH(1U, 0U);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("y_act", &c3_y_act, c3_f_sf_marshallOut,
    c3_e_sf_marshallIn);
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 30U, chartInstance->c3_sfEvent);
  c3_y_act = 0.0;
  _SFD_DATA_RANGE_CHECK(c3_y_act, 17U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 28U, chartInstance->c3_sfEvent);
  c3_y_act = (real_T)(*chartInstance->c3_LO_mode == Active);
  _SFD_DATA_RANGE_CHECK(c3_y_act, 17U);
  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CS_CALL(FUNCTION_INACTIVE_TAG, 30U, chartInstance->c3_sfEvent);
  _SFD_UNSET_DATA_VALUE_PTR(17U);
  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 30U, chartInstance->c3_sfEvent);
  return c3_y_act;
}

static real_T c3_LI_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  real_T c3_y_act;
  _SFD_SET_DATA_VALUE_PTR(18U, (void *)&c3_y_act);
  _SFD_CS_CALL(FUNCTION_ACTIVE_TAG, 29U, chartInstance->c3_sfEvent);
  _SFD_SYMBOL_SCOPE_PUSH(1U, 0U);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("y_act", &c3_y_act, c3_f_sf_marshallOut,
    c3_e_sf_marshallIn);
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 29U, chartInstance->c3_sfEvent);
  c3_y_act = 0.0;
  _SFD_DATA_RANGE_CHECK(c3_y_act, 18U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 30U, chartInstance->c3_sfEvent);
  c3_y_act = (real_T)(*chartInstance->c3_LI_mode == Active);
  _SFD_DATA_RANGE_CHECK(c3_y_act, 18U);
  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CS_CALL(FUNCTION_INACTIVE_TAG, 29U, chartInstance->c3_sfEvent);
  _SFD_UNSET_DATA_VALUE_PTR(18U);
  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 29U, chartInstance->c3_sfEvent);
  return c3_y_act;
}

static real_T c3_RO_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  real_T c3_y_act;
  _SFD_SET_DATA_VALUE_PTR(19U, (void *)&c3_y_act);
  _SFD_CS_CALL(FUNCTION_ACTIVE_TAG, 33U, chartInstance->c3_sfEvent);
  _SFD_SYMBOL_SCOPE_PUSH(1U, 0U);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("y_act", &c3_y_act, c3_f_sf_marshallOut,
    c3_e_sf_marshallIn);
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 33U, chartInstance->c3_sfEvent);
  c3_y_act = 0.0;
  _SFD_DATA_RANGE_CHECK(c3_y_act, 19U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 31U, chartInstance->c3_sfEvent);
  c3_y_act = (real_T)(*chartInstance->c3_RO_mode == Active);
  _SFD_DATA_RANGE_CHECK(c3_y_act, 19U);
  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CS_CALL(FUNCTION_INACTIVE_TAG, 33U, chartInstance->c3_sfEvent);
  _SFD_UNSET_DATA_VALUE_PTR(19U);
  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 33U, chartInstance->c3_sfEvent);
  return c3_y_act;
}

static real_T c3_RI_act(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  real_T c3_y_act;
  _SFD_SET_DATA_VALUE_PTR(20U, (void *)&c3_y_act);
  _SFD_CS_CALL(FUNCTION_ACTIVE_TAG, 32U, chartInstance->c3_sfEvent);
  _SFD_SYMBOL_SCOPE_PUSH(1U, 0U);
  _SFD_SYMBOL_SCOPE_ADD_IMPORTABLE("y_act", &c3_y_act, c3_f_sf_marshallOut,
    c3_e_sf_marshallIn);
  _SFD_CS_CALL(STATE_ENTER_DURING_FUNCTION_TAG, 32U, chartInstance->c3_sfEvent);
  c3_y_act = 0.0;
  _SFD_DATA_RANGE_CHECK(c3_y_act, 20U);
  _SFD_CT_CALL(TRANSITION_ACTIVE_TAG, 24U, chartInstance->c3_sfEvent);
  c3_y_act = (real_T)(*chartInstance->c3_RI_mode == Active);
  _SFD_DATA_RANGE_CHECK(c3_y_act, 20U);
  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CS_CALL(FUNCTION_INACTIVE_TAG, 32U, chartInstance->c3_sfEvent);
  _SFD_UNSET_DATA_VALUE_PTR(20U);
  _SFD_CS_CALL(EXIT_OUT_OF_FUNCTION_TAG, 32U, chartInstance->c3_sfEvent);
  return c3_y_act;
}

static const mxArray *c3_sf_marshallOut(void *chartInstanceVoid, void *c3_inData)
{
  const mxArray *c3_mxArrayOutData;
  int32_T c3_b_u;
  const mxArray *c3_y = NULL;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_mxArrayOutData = NULL;
  c3_mxArrayOutData = NULL;
  c3_b_u = *(int32_T *)c3_inData;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_create("y", &c3_b_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_mxArrayOutData, c3_y, false);
  return c3_mxArrayOutData;
}

static int32_T c3_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_sfEvent, const char_T *c3_identifier)
{
  int32_T c3_y;
  emlrtMsgIdentifier c3_thisId;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_b_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_b_sfEvent),
    &c3_thisId);
  sf_mex_destroy(&c3_b_sfEvent);
  return c3_y;
}

static int32_T c3_b_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId)
{
  int32_T c3_y;
  int32_T c3_i0;
  (void)chartInstance;
  sf_mex_import(c3_parentId, sf_mex_dup(c3_b_u), &c3_i0, 1, 6, 0U, 0, 0U, 0);
  c3_y = c3_i0;
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static void c3_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData)
{
  const mxArray *c3_b_sfEvent;
  const char_T *c3_identifier;
  emlrtMsgIdentifier c3_thisId;
  int32_T c3_y;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_b_sfEvent = sf_mex_dup(c3_mxArrayInData);
  c3_identifier = c3_varName;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_b_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_b_sfEvent),
    &c3_thisId);
  sf_mex_destroy(&c3_b_sfEvent);
  *(int32_T *)c3_outData = c3_y;
  sf_mex_destroy(&c3_mxArrayInData);
}

static const mxArray *c3_b_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData)
{
  const mxArray *c3_mxArrayOutData;
  uint8_T c3_b_u;
  const mxArray *c3_y = NULL;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_mxArrayOutData = NULL;
  c3_mxArrayOutData = NULL;
  c3_b_u = *(uint8_T *)c3_inData;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_create("y", &c3_b_u, 3, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_mxArrayOutData, c3_y, false);
  return c3_mxArrayOutData;
}

static uint8_T c3_c_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_tp_Actuators, const char_T *c3_identifier)
{
  uint8_T c3_y;
  emlrtMsgIdentifier c3_thisId;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_d_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_b_tp_Actuators),
    &c3_thisId);
  sf_mex_destroy(&c3_b_tp_Actuators);
  return c3_y;
}

static uint8_T c3_d_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId)
{
  uint8_T c3_y;
  uint8_T c3_u0;
  (void)chartInstance;
  sf_mex_import(c3_parentId, sf_mex_dup(c3_b_u), &c3_u0, 1, 3, 0U, 0, 0U, 0);
  c3_y = c3_u0;
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static void c3_b_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData)
{
  const mxArray *c3_b_tp_Actuators;
  const char_T *c3_identifier;
  emlrtMsgIdentifier c3_thisId;
  uint8_T c3_y;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_b_tp_Actuators = sf_mex_dup(c3_mxArrayInData);
  c3_identifier = c3_varName;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_d_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_b_tp_Actuators),
    &c3_thisId);
  sf_mex_destroy(&c3_b_tp_Actuators);
  *(uint8_T *)c3_outData = c3_y;
  sf_mex_destroy(&c3_mxArrayInData);
}

static const mxArray *c3_c_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData)
{
  const mxArray *c3_mxArrayOutData;
  sf_aircraft_ModeType c3_b_u;
  const mxArray *c3_y = NULL;
  int32_T c3_c_u;
  const mxArray *c3_b_y = NULL;
  const mxArray *c3_m4 = NULL;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_mxArrayOutData = NULL;
  c3_mxArrayOutData = NULL;
  c3_b_u = *(sf_aircraft_ModeType *)c3_inData;
  c3_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv0, c3_iv0);
  c3_c_u = (int32_T)c3_b_u;
  c3_b_y = NULL;
  sf_mex_assign(&c3_b_y, sf_mex_create("y", &c3_c_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m4, c3_b_y, false);
  sf_mex_assign(&c3_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m4), false);
  sf_mex_destroy(&c3_m4);
  sf_mex_assign(&c3_mxArrayOutData, c3_y, false);
  return c3_mxArrayOutData;
}

static sf_aircraft_ModeType c3_e_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray
   *c3_b_LO_mode, const char_T *c3_identifier)
{
  sf_aircraft_ModeType c3_y;
  emlrtMsgIdentifier c3_thisId;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_f_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_b_LO_mode),
    &c3_thisId);
  sf_mex_destroy(&c3_b_LO_mode);
  return c3_y;
}

static sf_aircraft_ModeType c3_f_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray *c3_b_u,
   const emlrtMsgIdentifier *c3_parentId)
{
  sf_aircraft_ModeType c3_y;
  (void)chartInstance;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv0, c3_iv0);
  sf_mex_check_builtin(c3_parentId, c3_b_u, "sf_aircraft_ModeType", 0, 0U, NULL);
  c3_y = (sf_aircraft_ModeType)sf_mex_get_enum_element(c3_b_u, 0);
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static void c3_c_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData)
{
  const mxArray *c3_b_LO_mode;
  const char_T *c3_identifier;
  emlrtMsgIdentifier c3_thisId;
  sf_aircraft_ModeType c3_y;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_b_LO_mode = sf_mex_dup(c3_mxArrayInData);
  c3_identifier = c3_varName;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_f_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_b_LO_mode),
    &c3_thisId);
  sf_mex_destroy(&c3_b_LO_mode);
  *(sf_aircraft_ModeType *)c3_outData = c3_y;
  sf_mex_destroy(&c3_mxArrayInData);
}

static const mxArray *c3_u_bus_io(void *chartInstanceVoid, void *c3_pData)
{
  const mxArray *c3_mxVal;
  int32_T c3_i1;
  int32_T c3_i2;
  c3_PositionBus c3_tmp;
  int32_T c3_i3;
  int32_T c3_i4;
  int32_T c3_i5;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_mxVal = NULL;
  c3_mxVal = NULL;
  for (c3_i1 = 0; c3_i1 < 2; c3_i1++) {
    c3_tmp.L_pos[c3_i1] = ((real_T *)&((char_T *)(c3_PositionBus *)c3_pData)[0])
      [c3_i1];
  }

  for (c3_i2 = 0; c3_i2 < 2; c3_i2++) {
    c3_tmp.L_pos_fail[c3_i2] = ((boolean_T *)&((char_T *)(c3_PositionBus *)
      c3_pData)[16])[c3_i2];
  }

  for (c3_i3 = 0; c3_i3 < 2; c3_i3++) {
    c3_tmp.R_pos[c3_i3] = ((real_T *)&((char_T *)(c3_PositionBus *)c3_pData)[24])
      [c3_i3];
  }

  for (c3_i4 = 0; c3_i4 < 2; c3_i4++) {
    c3_tmp.R_pos_fail[c3_i4] = ((boolean_T *)&((char_T *)(c3_PositionBus *)
      c3_pData)[40])[c3_i4];
  }

  c3_tmp.H1_press = *(real_T *)&((char_T *)(c3_PositionBus *)c3_pData)[48];
  c3_tmp.H2_press = *(real_T *)&((char_T *)(c3_PositionBus *)c3_pData)[56];
  c3_tmp.H3_press = *(real_T *)&((char_T *)(c3_PositionBus *)c3_pData)[64];
  for (c3_i5 = 0; c3_i5 < 3; c3_i5++) {
    c3_tmp.low_press[c3_i5] = ((boolean_T *)&((char_T *)(c3_PositionBus *)
      c3_pData)[72])[c3_i5];
  }

  sf_mex_assign(&c3_mxVal, c3_d_sf_marshallOut(chartInstance, &c3_tmp), false);
  return c3_mxVal;
}

static const mxArray *c3_d_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData)
{
  const mxArray *c3_mxArrayOutData;
  c3_PositionBus c3_b_u;
  const mxArray *c3_y = NULL;
  int32_T c3_i6;
  const mxArray *c3_b_y = NULL;
  real_T c3_c_u[2];
  int32_T c3_i7;
  const mxArray *c3_c_y = NULL;
  boolean_T c3_d_u[2];
  int32_T c3_i8;
  const mxArray *c3_d_y = NULL;
  int32_T c3_i9;
  const mxArray *c3_e_y = NULL;
  real_T c3_e_u;
  const mxArray *c3_f_y = NULL;
  real_T c3_f_u;
  const mxArray *c3_g_y = NULL;
  real_T c3_g_u;
  const mxArray *c3_h_y = NULL;
  int32_T c3_i10;
  const mxArray *c3_i_y = NULL;
  boolean_T c3_h_u[3];
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_mxArrayOutData = NULL;
  c3_mxArrayOutData = NULL;
  c3_b_u = *(c3_PositionBus *)c3_inData;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_createstruct("structure", 2, 1, 1), false);
  for (c3_i6 = 0; c3_i6 < 2; c3_i6++) {
    c3_c_u[c3_i6] = c3_b_u.L_pos[c3_i6];
  }

  c3_b_y = NULL;
  sf_mex_assign(&c3_b_y, sf_mex_create("y", c3_c_u, 0, 0U, 1U, 0U, 1, 2), false);
  sf_mex_addfield(c3_y, c3_b_y, "L_pos", "L_pos", 0);
  for (c3_i7 = 0; c3_i7 < 2; c3_i7++) {
    c3_d_u[c3_i7] = c3_b_u.L_pos_fail[c3_i7];
  }

  c3_c_y = NULL;
  sf_mex_assign(&c3_c_y, sf_mex_create("y", c3_d_u, 11, 0U, 1U, 0U, 1, 2), false);
  sf_mex_addfield(c3_y, c3_c_y, "L_pos_fail", "L_pos_fail", 0);
  for (c3_i8 = 0; c3_i8 < 2; c3_i8++) {
    c3_c_u[c3_i8] = c3_b_u.R_pos[c3_i8];
  }

  c3_d_y = NULL;
  sf_mex_assign(&c3_d_y, sf_mex_create("y", c3_c_u, 0, 0U, 1U, 0U, 1, 2), false);
  sf_mex_addfield(c3_y, c3_d_y, "R_pos", "R_pos", 0);
  for (c3_i9 = 0; c3_i9 < 2; c3_i9++) {
    c3_d_u[c3_i9] = c3_b_u.R_pos_fail[c3_i9];
  }

  c3_e_y = NULL;
  sf_mex_assign(&c3_e_y, sf_mex_create("y", c3_d_u, 11, 0U, 1U, 0U, 1, 2), false);
  sf_mex_addfield(c3_y, c3_e_y, "R_pos_fail", "R_pos_fail", 0);
  c3_e_u = c3_b_u.H1_press;
  c3_f_y = NULL;
  sf_mex_assign(&c3_f_y, sf_mex_create("y", &c3_e_u, 0, 0U, 0U, 0U, 0), false);
  sf_mex_addfield(c3_y, c3_f_y, "H1_press", "H1_press", 0);
  c3_f_u = c3_b_u.H2_press;
  c3_g_y = NULL;
  sf_mex_assign(&c3_g_y, sf_mex_create("y", &c3_f_u, 0, 0U, 0U, 0U, 0), false);
  sf_mex_addfield(c3_y, c3_g_y, "H2_press", "H2_press", 0);
  c3_g_u = c3_b_u.H3_press;
  c3_h_y = NULL;
  sf_mex_assign(&c3_h_y, sf_mex_create("y", &c3_g_u, 0, 0U, 0U, 0U, 0), false);
  sf_mex_addfield(c3_y, c3_h_y, "H3_press", "H3_press", 0);
  for (c3_i10 = 0; c3_i10 < 3; c3_i10++) {
    c3_h_u[c3_i10] = c3_b_u.low_press[c3_i10];
  }

  c3_i_y = NULL;
  sf_mex_assign(&c3_i_y, sf_mex_create("y", c3_h_u, 11, 0U, 1U, 0U, 1, 3), false);
  sf_mex_addfield(c3_y, c3_i_y, "low_press", "low_press", 0);
  sf_mex_assign(&c3_mxArrayOutData, c3_y, false);
  return c3_mxArrayOutData;
}

static const mxArray *c3_e_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData)
{
  const mxArray *c3_mxArrayOutData;
  boolean_T c3_b_u;
  const mxArray *c3_y = NULL;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_mxArrayOutData = NULL;
  c3_mxArrayOutData = NULL;
  c3_b_u = *(boolean_T *)c3_inData;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_create("y", &c3_b_u, 11, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_mxArrayOutData, c3_y, false);
  return c3_mxArrayOutData;
}

static boolean_T c3_g_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId)
{
  boolean_T c3_y;
  boolean_T c3_b0;
  (void)chartInstance;
  sf_mex_import(c3_parentId, sf_mex_dup(c3_b_u), &c3_b0, 1, 11, 0U, 0, 0U, 0);
  c3_y = c3_b0;
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static void c3_d_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData)
{
  const mxArray *c3_aVarTruthTableCondition_1;
  const char_T *c3_identifier;
  emlrtMsgIdentifier c3_thisId;
  boolean_T c3_y;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_aVarTruthTableCondition_1 = sf_mex_dup(c3_mxArrayInData);
  c3_identifier = c3_varName;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_g_emlrt_marshallIn(chartInstance, sf_mex_dup
    (c3_aVarTruthTableCondition_1), &c3_thisId);
  sf_mex_destroy(&c3_aVarTruthTableCondition_1);
  *(boolean_T *)c3_outData = c3_y;
  sf_mex_destroy(&c3_mxArrayInData);
}

static const mxArray *c3_f_sf_marshallOut(void *chartInstanceVoid, void
  *c3_inData)
{
  const mxArray *c3_mxArrayOutData;
  real_T c3_b_u;
  const mxArray *c3_y = NULL;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_mxArrayOutData = NULL;
  c3_mxArrayOutData = NULL;
  c3_b_u = *(real_T *)c3_inData;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_create("y", &c3_b_u, 0, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_mxArrayOutData, c3_y, false);
  return c3_mxArrayOutData;
}

static real_T c3_h_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId)
{
  real_T c3_y;
  real_T c3_d28;
  (void)chartInstance;
  sf_mex_import(c3_parentId, sf_mex_dup(c3_b_u), &c3_d28, 1, 0, 0U, 0, 0U, 0);
  c3_y = c3_d28;
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static void c3_e_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c3_mxArrayInData, const char_T *c3_varName, void *c3_outData)
{
  const mxArray *c3_y_act;
  const char_T *c3_identifier;
  emlrtMsgIdentifier c3_thisId;
  real_T c3_y;
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)chartInstanceVoid;
  c3_y_act = sf_mex_dup(c3_mxArrayInData);
  c3_identifier = c3_varName;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_h_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_y_act), &c3_thisId);
  sf_mex_destroy(&c3_y_act);
  *(real_T *)c3_outData = c3_y;
  sf_mex_destroy(&c3_mxArrayInData);
}

static const mxArray *c3_i_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_setSimStateSideEffectsInfo, const char_T
  *c3_identifier)
{
  const mxArray *c3_y = NULL;
  emlrtMsgIdentifier c3_thisId;
  c3_y = NULL;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  sf_mex_assign(&c3_y, c3_j_emlrt_marshallIn(chartInstance, sf_mex_dup
    (c3_b_setSimStateSideEffectsInfo), &c3_thisId), false);
  sf_mex_destroy(&c3_b_setSimStateSideEffectsInfo);
  return c3_y;
}

static const mxArray *c3_j_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId)
{
  const mxArray *c3_y = NULL;
  (void)chartInstance;
  (void)c3_parentId;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_duplicatearraysafe(&c3_b_u), false);
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static const mxArray *sf_get_hover_data_for_msg
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, int32_T c3_ssid)
{
  (void)chartInstance;
  (void)c3_ssid;
  return NULL;
}

static void c3_init_sf_message_store_memory(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  (void)chartInstance;
}

static int32_T c3__s32_add__(SFc3_sf_aircraft_faultInstanceStruct *chartInstance,
  int32_T c3_b, int32_T c3_c, uint32_T c3_ssid_src_loc, int32_T
  c3_offset_src_loc, int32_T c3_length_src_loc)
{
  int32_T c3_a;
  (void)chartInstance;
  c3_a = c3_b + c3_c;
  if (((c3_a ^ c3_b) & (c3_a ^ c3_c)) < 0) {
    _SFD_OVERFLOW_DETECTION(SFDB_OVERFLOW, c3_ssid_src_loc, c3_offset_src_loc,
      c3_length_src_loc);
  }

  return c3_a;
}

static void init_dsm_address_info(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  (void)chartInstance;
}

static void init_simulink_io_address(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  chartInstance->c3_fEmlrtCtx = (void *)sfrtGetEmlrtCtx(chartInstance->S);
  chartInstance->c3_LO_mode = (sf_aircraft_ModeType *)
    ssGetOutputPortSignal_wrapper(chartInstance->S, 1);
  chartInstance->c3_RO_mode = (sf_aircraft_ModeType *)
    ssGetOutputPortSignal_wrapper(chartInstance->S, 2);
  chartInstance->c3_LI_mode = (sf_aircraft_ModeType *)
    ssGetOutputPortSignal_wrapper(chartInstance->S, 3);
  chartInstance->c3_RI_mode = (sf_aircraft_ModeType *)
    ssGetOutputPortSignal_wrapper(chartInstance->S, 4);
  chartInstance->c3_u = (c3_PositionBus *)ssGetInputPortSignal_wrapper
    (chartInstance->S, 0);
}

/* SFunction Glue Code */
#ifdef utFree
#undef utFree
#endif

#ifdef utMalloc
#undef utMalloc
#endif

#ifdef __cplusplus

extern "C" void *utMalloc(size_t size);
extern "C" void utFree(void*);

#else

extern void *utMalloc(size_t size);
extern void utFree(void*);

#endif

void sf_c3_sf_aircraft_fault_get_check_sum(mxArray *plhs[])
{
  ((real_T *)mxGetPr((plhs[0])))[0] = (real_T)(1581481309U);
  ((real_T *)mxGetPr((plhs[0])))[1] = (real_T)(2232119605U);
  ((real_T *)mxGetPr((plhs[0])))[2] = (real_T)(3730683927U);
  ((real_T *)mxGetPr((plhs[0])))[3] = (real_T)(2629605303U);
}

mxArray* sf_c3_sf_aircraft_fault_get_post_codegen_info(void);
mxArray *sf_c3_sf_aircraft_fault_get_autoinheritance_info(void)
{
  const char *autoinheritanceFields[] = { "checksum", "inputs", "parameters",
    "outputs", "locals", "postCodegenInfo" };

  mxArray *mxAutoinheritanceInfo = mxCreateStructMatrix(1, 1, sizeof
    (autoinheritanceFields)/sizeof(autoinheritanceFields[0]),
    autoinheritanceFields);

  {
    mxArray *mxChecksum = mxCreateString("atEIAqEuDRVE6Fada78GiC");
    mxSetField(mxAutoinheritanceInfo,0,"checksum",mxChecksum);
  }

  {
    const char *dataFields[] = { "size", "type", "complexity" };

    mxArray *mxData = mxCreateStructMatrix(1,1,3,dataFields);

    {
      mxArray *mxSize = mxCreateDoubleMatrix(1,0,mxREAL);
      double *pr = mxGetPr(mxSize);
      mxSetField(mxData,0,"size",mxSize);
    }

    {
      const char *typeFields[] = { "base", "fixpt", "isFixedPointType" };

      mxArray *mxType = mxCreateStructMatrix(1,1,sizeof(typeFields)/sizeof
        (typeFields[0]),typeFields);
      mxSetField(mxType,0,"base",mxCreateDoubleScalar(13));
      mxSetField(mxType,0,"fixpt",mxCreateDoubleMatrix(0,0,mxREAL));
      mxSetField(mxType,0,"isFixedPointType",mxCreateDoubleScalar(0));
      mxSetField(mxData,0,"type",mxType);
    }

    mxSetField(mxData,0,"complexity",mxCreateDoubleScalar(0));
    mxSetField(mxAutoinheritanceInfo,0,"inputs",mxData);
  }

  {
    mxSetField(mxAutoinheritanceInfo,0,"parameters",mxCreateDoubleMatrix(0,0,
                mxREAL));
  }

  {
    const char *dataFields[] = { "size", "type", "complexity" };

    mxArray *mxData = mxCreateStructMatrix(1,4,3,dataFields);

    {
      mxArray *mxSize = mxCreateDoubleMatrix(1,0,mxREAL);
      double *pr = mxGetPr(mxSize);
      mxSetField(mxData,0,"size",mxSize);
    }

    {
      const char *typeFields[] = { "base", "fixpt", "isFixedPointType" };

      mxArray *mxType = mxCreateStructMatrix(1,1,sizeof(typeFields)/sizeof
        (typeFields[0]),typeFields);
      mxSetField(mxType,0,"base",mxCreateDoubleScalar(14));
      mxSetField(mxType,0,"fixpt",mxCreateDoubleMatrix(0,0,mxREAL));
      mxSetField(mxType,0,"isFixedPointType",mxCreateDoubleScalar(0));
      mxSetField(mxData,0,"type",mxType);
    }

    mxSetField(mxData,0,"complexity",mxCreateDoubleScalar(0));

    {
      mxArray *mxSize = mxCreateDoubleMatrix(1,0,mxREAL);
      double *pr = mxGetPr(mxSize);
      mxSetField(mxData,1,"size",mxSize);
    }

    {
      const char *typeFields[] = { "base", "fixpt", "isFixedPointType" };

      mxArray *mxType = mxCreateStructMatrix(1,1,sizeof(typeFields)/sizeof
        (typeFields[0]),typeFields);
      mxSetField(mxType,0,"base",mxCreateDoubleScalar(14));
      mxSetField(mxType,0,"fixpt",mxCreateDoubleMatrix(0,0,mxREAL));
      mxSetField(mxType,0,"isFixedPointType",mxCreateDoubleScalar(0));
      mxSetField(mxData,1,"type",mxType);
    }

    mxSetField(mxData,1,"complexity",mxCreateDoubleScalar(0));

    {
      mxArray *mxSize = mxCreateDoubleMatrix(1,0,mxREAL);
      double *pr = mxGetPr(mxSize);
      mxSetField(mxData,2,"size",mxSize);
    }

    {
      const char *typeFields[] = { "base", "fixpt", "isFixedPointType" };

      mxArray *mxType = mxCreateStructMatrix(1,1,sizeof(typeFields)/sizeof
        (typeFields[0]),typeFields);
      mxSetField(mxType,0,"base",mxCreateDoubleScalar(14));
      mxSetField(mxType,0,"fixpt",mxCreateDoubleMatrix(0,0,mxREAL));
      mxSetField(mxType,0,"isFixedPointType",mxCreateDoubleScalar(0));
      mxSetField(mxData,2,"type",mxType);
    }

    mxSetField(mxData,2,"complexity",mxCreateDoubleScalar(0));

    {
      mxArray *mxSize = mxCreateDoubleMatrix(1,0,mxREAL);
      double *pr = mxGetPr(mxSize);
      mxSetField(mxData,3,"size",mxSize);
    }

    {
      const char *typeFields[] = { "base", "fixpt", "isFixedPointType" };

      mxArray *mxType = mxCreateStructMatrix(1,1,sizeof(typeFields)/sizeof
        (typeFields[0]),typeFields);
      mxSetField(mxType,0,"base",mxCreateDoubleScalar(14));
      mxSetField(mxType,0,"fixpt",mxCreateDoubleMatrix(0,0,mxREAL));
      mxSetField(mxType,0,"isFixedPointType",mxCreateDoubleScalar(0));
      mxSetField(mxData,3,"type",mxType);
    }

    mxSetField(mxData,3,"complexity",mxCreateDoubleScalar(0));
    mxSetField(mxAutoinheritanceInfo,0,"outputs",mxData);
  }

  {
    mxSetField(mxAutoinheritanceInfo,0,"locals",mxCreateDoubleMatrix(0,0,mxREAL));
  }

  {
    mxArray* mxPostCodegenInfo = sf_c3_sf_aircraft_fault_get_post_codegen_info();
    mxSetField(mxAutoinheritanceInfo,0,"postCodegenInfo",mxPostCodegenInfo);
  }

  return(mxAutoinheritanceInfo);
}

mxArray *sf_c3_sf_aircraft_fault_third_party_uses_info(void)
{
  mxArray * mxcell3p = mxCreateCellMatrix(1,0);
  return(mxcell3p);
}

mxArray *sf_c3_sf_aircraft_fault_jit_fallback_info(void)
{
  const char *infoFields[] = { "fallbackType", "fallbackReason",
    "hiddenFallbackType", "hiddenFallbackReason", "incompatibleSymbol" };

  mxArray *mxInfo = mxCreateStructMatrix(1, 1, 5, infoFields);
  mxArray *fallbackType = mxCreateString("early");
  mxArray *fallbackReason = mxCreateString("imported_enum");
  mxArray *hiddenFallbackType = mxCreateString("");
  mxArray *hiddenFallbackReason = mxCreateString("");
  mxArray *incompatibleSymbol = mxCreateString("sf_aircraft_ModeType");
  mxSetField(mxInfo, 0, infoFields[0], fallbackType);
  mxSetField(mxInfo, 0, infoFields[1], fallbackReason);
  mxSetField(mxInfo, 0, infoFields[2], hiddenFallbackType);
  mxSetField(mxInfo, 0, infoFields[3], hiddenFallbackReason);
  mxSetField(mxInfo, 0, infoFields[4], incompatibleSymbol);
  return mxInfo;
}

mxArray *sf_c3_sf_aircraft_fault_updateBuildInfo_args_info(void)
{
  mxArray *mxBIArgs = mxCreateCellMatrix(1,0);
  return mxBIArgs;
}

mxArray* sf_c3_sf_aircraft_fault_get_post_codegen_info(void)
{
  const char* fieldNames[] = { "exportedFunctionsUsedByThisChart",
    "exportedFunctionsChecksum" };

  mwSize dims[2] = { 1, 1 };

  mxArray* mxPostCodegenInfo = mxCreateStructArray(2, dims, sizeof(fieldNames)/
    sizeof(fieldNames[0]), fieldNames);

  {
    mxArray* mxExportedFunctionsChecksum = mxCreateString("");
    mwSize exp_dims[2] = { 0, 1 };

    mxArray* mxExportedFunctionsUsedByThisChart = mxCreateCellArray(2, exp_dims);
    mxSetField(mxPostCodegenInfo, 0, "exportedFunctionsUsedByThisChart",
               mxExportedFunctionsUsedByThisChart);
    mxSetField(mxPostCodegenInfo, 0, "exportedFunctionsChecksum",
               mxExportedFunctionsChecksum);
  }

  return mxPostCodegenInfo;
}

static const mxArray *sf_get_sim_state_info_c3_sf_aircraft_fault(void)
{
  const char *infoFields[] = { "chartChecksum", "varInfo" };

  mxArray *mxInfo = mxCreateStructMatrix(1, 1, 2, infoFields);
  const char *infoEncStr[] = {
    "100 S1x10'type','srcId','name','auxInfo'{{M[2],M[920],T\"LI_mode\",},{M[2],M[918],T\"LO_mode\",},{M[2],M[921],T\"RI_mode\",},{M[2],M[919],T\"RO_mode\",},{M[3],M[212],T\"fails\",},{M[3],M[213],T\"fails\",},{M[3],M[214],T\"fails\",},{M[3],M[215],T\"fails\",},{M[8],M[0],T\"is_active_c3_sf_aircraft_fault\",},{M[8],M[4],T\"is_active_LO\",}}",
    "100 S1x8'type','srcId','name','auxInfo'{{M[8],M[15],T\"is_active_RO\",},{M[8],M[22],T\"is_active_LI\",},{M[8],M[29],T\"is_active_RI\",},{M[9],M[0],T\"is_c3_sf_aircraft_fault\",},{M[9],M[4],T\"is_LO\",},{M[9],M[15],T\"is_RO\",},{M[9],M[22],T\"is_LI\",},{M[9],M[29],T\"is_RI\",}}"
  };

  mxArray *mxVarInfo = sf_mex_decode_encoded_mx_struct_array(infoEncStr, 18, 10);
  mxArray *mxChecksum = mxCreateDoubleMatrix(1, 4, mxREAL);
  sf_c3_sf_aircraft_fault_get_check_sum(&mxChecksum);
  mxSetField(mxInfo, 0, infoFields[0], mxChecksum);
  mxSetField(mxInfo, 0, infoFields[1], mxVarInfo);
  return mxInfo;
}

static const mxArray* sf_opaque_get_hover_data_for_msg(void* chartInstance,
  int32_T msgSSID)
{
  return sf_get_hover_data_for_msg( (SFc3_sf_aircraft_faultInstanceStruct *)
    chartInstance, msgSSID);
}

static void chart_debug_initialization(SimStruct *S, unsigned int
  fullDebuggerInitialization)
{
  if (!sim_mode_is_rtw_gen(S)) {
    SFc3_sf_aircraft_faultInstanceStruct *chartInstance =
      (SFc3_sf_aircraft_faultInstanceStruct *)sf_get_chart_instance_ptr(S);
    if (ssIsFirstInitCond(S) && fullDebuggerInitialization==1) {
      /* do this only if simulation is starting */
      {
        unsigned int chartAlreadyPresent;
        chartAlreadyPresent = sf_debug_initialize_chart
          (sfGlobalDebugInstanceStruct,
           _sf_aircraft_faultMachineNumber_,
           3,
           35,
           104,
           0,
           21,
           3,
           0,
           0,
           0,
           0,
           &chartInstance->chartNumber,
           &chartInstance->instanceNumber,
           (void *)S);

        /* Each instance must initialize its own list of scripts */
        init_script_number_translation(_sf_aircraft_faultMachineNumber_,
          chartInstance->chartNumber,chartInstance->instanceNumber);
        if (chartAlreadyPresent==0) {
          /* this is the first instance */
          sf_debug_set_chart_disable_implicit_casting
            (sfGlobalDebugInstanceStruct,_sf_aircraft_faultMachineNumber_,
             chartInstance->chartNumber,1);
          sf_debug_set_chart_event_thresholds(sfGlobalDebugInstanceStruct,
            _sf_aircraft_faultMachineNumber_,
            chartInstance->chartNumber,
            3,
            3,
            3);
          _SFD_SET_DATA_PROPS(0,0,0,0,"fails");
          _SFD_SET_DATA_PROPS(1,0,0,0,"fails");
          _SFD_SET_DATA_PROPS(2,0,0,0,"fails");
          _SFD_SET_DATA_PROPS(3,0,0,0,"fails");
          _SFD_SET_DATA_PROPS(4,1,1,0,"u");
          _SFD_SET_DATA_PROPS(5,2,0,1,"LO_mode");
          _SFD_SET_DATA_PROPS(6,2,0,1,"RO_mode");
          _SFD_SET_DATA_PROPS(7,2,0,1,"LI_mode");
          _SFD_SET_DATA_PROPS(8,2,0,1,"RI_mode");
          _SFD_SET_DATA_PROPS(9,6,0,0,"");
          _SFD_SET_DATA_PROPS(10,6,0,0,"");
          _SFD_SET_DATA_PROPS(11,6,0,0,"");
          _SFD_SET_DATA_PROPS(12,6,0,0,"");
          _SFD_SET_DATA_PROPS(13,6,0,0,"");
          _SFD_SET_DATA_PROPS(14,6,0,0,"");
          _SFD_SET_DATA_PROPS(15,6,0,0,"");
          _SFD_SET_DATA_PROPS(16,6,0,0,"");
          _SFD_SET_DATA_PROPS(17,9,0,0,"");
          _SFD_SET_DATA_PROPS(18,9,0,0,"");
          _SFD_SET_DATA_PROPS(19,9,0,0,"");
          _SFD_SET_DATA_PROPS(20,9,0,0,"");
          _SFD_EVENT_SCOPE(0,0);
          _SFD_EVENT_SCOPE(1,0);
          _SFD_EVENT_SCOPE(2,0);
          _SFD_STATE_INFO(0,1,0);
          _SFD_STATE_INFO(1,0,1);
          _SFD_STATE_INFO(2,0,0);
          _SFD_STATE_INFO(3,0,0);
          _SFD_STATE_INFO(4,0,0);
          _SFD_STATE_INFO(5,0,0);
          _SFD_STATE_INFO(6,0,0);
          _SFD_STATE_INFO(7,0,0);
          _SFD_STATE_INFO(8,0,1);
          _SFD_STATE_INFO(9,0,0);
          _SFD_STATE_INFO(10,0,0);
          _SFD_STATE_INFO(11,0,0);
          _SFD_STATE_INFO(12,0,0);
          _SFD_STATE_INFO(13,0,0);
          _SFD_STATE_INFO(14,0,0);
          _SFD_STATE_INFO(15,0,1);
          _SFD_STATE_INFO(16,0,0);
          _SFD_STATE_INFO(17,0,0);
          _SFD_STATE_INFO(18,0,0);
          _SFD_STATE_INFO(19,0,0);
          _SFD_STATE_INFO(20,0,0);
          _SFD_STATE_INFO(21,0,0);
          _SFD_STATE_INFO(22,0,1);
          _SFD_STATE_INFO(23,0,0);
          _SFD_STATE_INFO(24,0,0);
          _SFD_STATE_INFO(25,0,0);
          _SFD_STATE_INFO(26,0,0);
          _SFD_STATE_INFO(27,0,0);
          _SFD_STATE_INFO(28,0,0);
          _SFD_STATE_INFO(29,0,2);
          _SFD_STATE_INFO(30,0,2);
          _SFD_STATE_INFO(31,0,2);
          _SFD_STATE_INFO(32,0,2);
          _SFD_STATE_INFO(33,0,2);
          _SFD_STATE_INFO(34,0,2);
          _SFD_CH_SUBSTATE_COUNT(1);
          _SFD_CH_SUBSTATE_DECOMP(0);
          _SFD_CH_SUBSTATE_INDEX(0,0);
          _SFD_ST_SUBSTATE_COUNT(0,4);
          _SFD_ST_SUBSTATE_INDEX(0,0,8);
          _SFD_ST_SUBSTATE_INDEX(0,1,22);
          _SFD_ST_SUBSTATE_INDEX(0,2,1);
          _SFD_ST_SUBSTATE_INDEX(0,3,15);
          _SFD_ST_SUBSTATE_COUNT(8,2);
          _SFD_ST_SUBSTATE_INDEX(8,0,9);
          _SFD_ST_SUBSTATE_INDEX(8,1,10);
          _SFD_ST_SUBSTATE_COUNT(9,0);
          _SFD_ST_SUBSTATE_COUNT(10,4);
          _SFD_ST_SUBSTATE_INDEX(10,0,11);
          _SFD_ST_SUBSTATE_INDEX(10,1,12);
          _SFD_ST_SUBSTATE_INDEX(10,2,13);
          _SFD_ST_SUBSTATE_INDEX(10,3,14);
          _SFD_ST_SUBSTATE_COUNT(11,0);
          _SFD_ST_SUBSTATE_COUNT(12,0);
          _SFD_ST_SUBSTATE_COUNT(13,0);
          _SFD_ST_SUBSTATE_COUNT(14,0);
          _SFD_ST_SUBSTATE_COUNT(22,2);
          _SFD_ST_SUBSTATE_INDEX(22,0,23);
          _SFD_ST_SUBSTATE_INDEX(22,1,24);
          _SFD_ST_SUBSTATE_COUNT(23,0);
          _SFD_ST_SUBSTATE_COUNT(24,4);
          _SFD_ST_SUBSTATE_INDEX(24,0,25);
          _SFD_ST_SUBSTATE_INDEX(24,1,26);
          _SFD_ST_SUBSTATE_INDEX(24,2,27);
          _SFD_ST_SUBSTATE_INDEX(24,3,28);
          _SFD_ST_SUBSTATE_COUNT(25,0);
          _SFD_ST_SUBSTATE_COUNT(26,0);
          _SFD_ST_SUBSTATE_COUNT(27,0);
          _SFD_ST_SUBSTATE_COUNT(28,0);
          _SFD_ST_SUBSTATE_COUNT(1,2);
          _SFD_ST_SUBSTATE_INDEX(1,0,2);
          _SFD_ST_SUBSTATE_INDEX(1,1,3);
          _SFD_ST_SUBSTATE_COUNT(2,0);
          _SFD_ST_SUBSTATE_COUNT(3,4);
          _SFD_ST_SUBSTATE_INDEX(3,0,4);
          _SFD_ST_SUBSTATE_INDEX(3,1,5);
          _SFD_ST_SUBSTATE_INDEX(3,2,6);
          _SFD_ST_SUBSTATE_INDEX(3,3,7);
          _SFD_ST_SUBSTATE_COUNT(4,0);
          _SFD_ST_SUBSTATE_COUNT(5,0);
          _SFD_ST_SUBSTATE_COUNT(6,0);
          _SFD_ST_SUBSTATE_COUNT(7,0);
          _SFD_ST_SUBSTATE_COUNT(15,2);
          _SFD_ST_SUBSTATE_INDEX(15,0,16);
          _SFD_ST_SUBSTATE_INDEX(15,1,17);
          _SFD_ST_SUBSTATE_COUNT(16,0);
          _SFD_ST_SUBSTATE_COUNT(17,4);
          _SFD_ST_SUBSTATE_INDEX(17,0,18);
          _SFD_ST_SUBSTATE_INDEX(17,1,19);
          _SFD_ST_SUBSTATE_INDEX(17,2,20);
          _SFD_ST_SUBSTATE_INDEX(17,3,21);
          _SFD_ST_SUBSTATE_COUNT(18,0);
          _SFD_ST_SUBSTATE_COUNT(19,0);
          _SFD_ST_SUBSTATE_COUNT(20,0);
          _SFD_ST_SUBSTATE_COUNT(21,0);
        }

        _SFD_CV_INIT_CHART(1,0,0,0);

        {
          _SFD_CV_INIT_STATE(0,4,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(1,2,1,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(2,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(3,4,1,1,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(4,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(5,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(6,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(7,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(8,2,1,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(9,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(10,4,1,1,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(11,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(12,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(13,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(14,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(15,2,1,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(16,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(17,4,1,1,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(18,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(19,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(20,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(21,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(22,2,1,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(23,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(24,4,1,1,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(25,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(26,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(27,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(28,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(29,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(30,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(31,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(32,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(33,0,0,0,0,0,NULL,NULL);
        }

        {
          _SFD_CV_INIT_STATE(34,0,0,0,0,0,NULL,NULL);
        }

        _SFD_CV_INIT_TRANS(10,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(14,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartRelationalopMap[] = { 1 };

          static unsigned int sEndRelationalopMap[] = { 9 };

          static int sRelationalopEps[] = { 0 };

          static int sRelationalopType[] = { 5 };

          _SFD_CV_INIT_TRANSITION_RELATIONALOP(14,1,&(sStartRelationalopMap[0]),
            &(sEndRelationalopMap[0]),&(sRelationalopEps[0]),
            &(sRelationalopType[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0 };

          static unsigned int sEndGuardMap[] = { 11 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(9,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(15,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(6,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 11 };

          static unsigned int sEndGuardMap[] = { 10, 19 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -2 };

          _SFD_CV_INIT_TRANS(17,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 2, 16 };

          static unsigned int sEndGuardMap[] = { 10, 24 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -3 };

          _SFD_CV_INIT_TRANS(16,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(19,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(18,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0, 8 };

          static unsigned int sEndGuardMap[] = { 6, 15 };

          static int sPostFixPredicateTree[] = { 0, 1, -1, -3 };

          _SFD_CV_INIT_TRANS(11,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(27,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2 };

          static unsigned int sEndGuardMap[] = { 16 };

          static int sPostFixPredicateTree[] = { 0, -1 };

          _SFD_CV_INIT_TRANS(12,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),2,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(47,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(48,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartRelationalopMap[] = { 1 };

          static unsigned int sEndRelationalopMap[] = { 9 };

          static int sRelationalopEps[] = { 0 };

          static int sRelationalopType[] = { 5 };

          _SFD_CV_INIT_TRANSITION_RELATIONALOP(48,1,&(sStartRelationalopMap[0]),
            &(sEndRelationalopMap[0]),&(sRelationalopEps[0]),
            &(sRelationalopType[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0 };

          static unsigned int sEndGuardMap[] = { 11 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(49,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(50,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(51,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 11 };

          static unsigned int sEndGuardMap[] = { 10, 19 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -2 };

          _SFD_CV_INIT_TRANS(0,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(2,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 16 };

          static unsigned int sEndGuardMap[] = { 10, 24 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -3 };

          _SFD_CV_INIT_TRANS(22,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(23,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 2 };

          static unsigned int sEndGuardMap[] = { 16 };

          static int sPostFixPredicateTree[] = { 0, -1 };

          _SFD_CV_INIT_TRANS(7,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),2,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0, 8 };

          static unsigned int sEndGuardMap[] = { 6, 15 };

          static int sPostFixPredicateTree[] = { 0, 1, -1, -3 };

          _SFD_CV_INIT_TRANS(21,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(20,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(5,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(4,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartRelationalopMap[] = { 1 };

          static unsigned int sEndRelationalopMap[] = { 9 };

          static int sRelationalopEps[] = { 0 };

          static int sRelationalopType[] = { 5 };

          _SFD_CV_INIT_TRANSITION_RELATIONALOP(4,1,&(sStartRelationalopMap[0]),
            &(sEndRelationalopMap[0]),&(sRelationalopEps[0]),
            &(sRelationalopType[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0 };

          static unsigned int sEndGuardMap[] = { 11 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(3,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(1,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(46,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 11 };

          static unsigned int sEndGuardMap[] = { 10, 19 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -2 };

          _SFD_CV_INIT_TRANS(45,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(44,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(43,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 1, 15 };

          static unsigned int sEndGuardMap[] = { 9, 23 };

          static int sPostFixPredicateTree[] = { 0, 1, -3 };

          _SFD_CV_INIT_TRANS(42,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),3,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 2 };

          static unsigned int sEndGuardMap[] = { 16 };

          static int sPostFixPredicateTree[] = { 0, -1 };

          _SFD_CV_INIT_TRANS(39,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),2,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0, 8 };

          static unsigned int sEndGuardMap[] = { 6, 15 };

          static int sPostFixPredicateTree[] = { 0, 1, -1, -3 };

          _SFD_CV_INIT_TRANS(41,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(40,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(38,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(37,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartRelationalopMap[] = { 1 };

          static unsigned int sEndRelationalopMap[] = { 9 };

          static int sRelationalopEps[] = { 0 };

          static int sRelationalopType[] = { 5 };

          _SFD_CV_INIT_TRANSITION_RELATIONALOP(37,1,&(sStartRelationalopMap[0]),
            &(sEndRelationalopMap[0]),&(sRelationalopEps[0]),
            &(sRelationalopType[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0 };

          static unsigned int sEndGuardMap[] = { 11 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(36,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(35,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(34,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 11 };

          static unsigned int sEndGuardMap[] = { 10, 19 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -2 };

          _SFD_CV_INIT_TRANS(33,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(32,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 9 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(29,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 1, 15 };

          static unsigned int sEndGuardMap[] = { 9, 23 };

          static int sPostFixPredicateTree[] = { 0, 1, -3 };

          _SFD_CV_INIT_TRANS(26,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),3,
                             &(sPostFixPredicateTree[0]));
        }

        {
          static unsigned int sStartGuardMap[] = { 0, 8 };

          static unsigned int sEndGuardMap[] = { 6, 15 };

          static int sPostFixPredicateTree[] = { 0, 1, -1, -3 };

          _SFD_CV_INIT_TRANS(25,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(13,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2 };

          static unsigned int sEndGuardMap[] = { 16 };

          static int sPostFixPredicateTree[] = { 0, -1 };

          _SFD_CV_INIT_TRANS(8,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),2,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(52,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(53,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(54,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(55,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(56,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1, 31, 61 };

          static unsigned int sEndGuardMap[] = { 26, 56, 86 };

          static int sPostFixPredicateTree[] = { 0, 1, -1, -3, 2, -1, -3 };

          _SFD_CV_INIT_TRANS(57,3,&(sStartGuardMap[0]),&(sEndGuardMap[0]),7,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(58,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(59,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 26 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(60,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(61,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(62,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(63,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 31, 61, 91 };

          static unsigned int sEndGuardMap[] = { 27, 56, 86, 116 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -3, 2, -1, -3, 3, -1,
            -3 };

          _SFD_CV_INIT_TRANS(64,4,&(sStartGuardMap[0]),&(sEndGuardMap[0]),10,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(65,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(66,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 31 };

          static unsigned int sEndGuardMap[] = { 27, 56 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -3 };

          _SFD_CV_INIT_TRANS(67,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(68,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(69,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(70,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 26 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(71,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(72,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(73,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 26 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(74,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(75,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(76,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(77,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(78,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(79,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(80,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(81,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(82,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(83,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1, 31, 61 };

          static unsigned int sEndGuardMap[] = { 26, 56, 86 };

          static int sPostFixPredicateTree[] = { 0, 1, -1, -3, 2, -1, -3 };

          _SFD_CV_INIT_TRANS(84,3,&(sStartGuardMap[0]),&(sEndGuardMap[0]),7,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(85,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(86,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 26 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(87,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(88,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(89,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 31, 61, 91 };

          static unsigned int sEndGuardMap[] = { 27, 56, 86, 116 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -3, 2, -1, -3, 3, -1,
            -3 };

          _SFD_CV_INIT_TRANS(90,4,&(sStartGuardMap[0]),&(sEndGuardMap[0]),10,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(91,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(92,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 2, 31 };

          static unsigned int sEndGuardMap[] = { 27, 56 };

          static int sPostFixPredicateTree[] = { 0, -1, 1, -3 };

          _SFD_CV_INIT_TRANS(93,2,&(sStartGuardMap[0]),&(sEndGuardMap[0]),4,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(94,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(95,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 26 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(96,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(97,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(98,0,NULL,NULL,0,NULL);

        {
          static unsigned int sStartGuardMap[] = { 1 };

          static unsigned int sEndGuardMap[] = { 26 };

          static int sPostFixPredicateTree[] = { 0 };

          _SFD_CV_INIT_TRANS(99,1,&(sStartGuardMap[0]),&(sEndGuardMap[0]),1,
                             &(sPostFixPredicateTree[0]));
        }

        _SFD_CV_INIT_TRANS(100,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(101,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(102,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(103,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(28,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(30,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(31,0,NULL,NULL,0,NULL);
        _SFD_CV_INIT_TRANS(24,0,NULL,NULL,0,NULL);
        _SFD_SET_DATA_COMPILED_PROPS(0,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_sf_marshallOut,(MexInFcnForType)c3_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(1,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_sf_marshallOut,(MexInFcnForType)c3_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(2,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_sf_marshallOut,(MexInFcnForType)c3_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(3,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_sf_marshallOut,(MexInFcnForType)c3_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(4,SF_STRUCT,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_u_bus_io,(MexInFcnForType)NULL);
        _SFD_SET_DATA_COMPILED_PROPS(5,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_c_sf_marshallOut,(MexInFcnForType)c3_c_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(6,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_c_sf_marshallOut,(MexInFcnForType)c3_c_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(7,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_c_sf_marshallOut,(MexInFcnForType)c3_c_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(8,SF_INT32,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_c_sf_marshallOut,(MexInFcnForType)c3_c_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(9,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(10,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(11,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(12,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(13,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(14,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(15,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(16,SF_UINT8,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_e_sf_marshallOut,(MexInFcnForType)c3_d_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(17,SF_DOUBLE,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_f_sf_marshallOut,(MexInFcnForType)c3_e_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(18,SF_DOUBLE,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_f_sf_marshallOut,(MexInFcnForType)c3_e_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(19,SF_DOUBLE,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_f_sf_marshallOut,(MexInFcnForType)c3_e_sf_marshallIn);
        _SFD_SET_DATA_COMPILED_PROPS(20,SF_DOUBLE,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c3_f_sf_marshallOut,(MexInFcnForType)c3_e_sf_marshallIn);
        _SFD_SET_DATA_VALUE_PTR(9,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(10,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(11,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(12,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(13,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(14,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(15,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(16,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(17,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(18,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(19,(void *)(NULL));
        _SFD_SET_DATA_VALUE_PTR(20,(void *)(NULL));
      }
    } else {
      sf_debug_reset_current_state_configuration(sfGlobalDebugInstanceStruct,
        _sf_aircraft_faultMachineNumber_,chartInstance->chartNumber,
        chartInstance->instanceNumber);
    }
  }
}

static void chart_debug_initialize_data_addresses(SimStruct *S)
{
  if (!sim_mode_is_rtw_gen(S)) {
    SFc3_sf_aircraft_faultInstanceStruct *chartInstance =
      (SFc3_sf_aircraft_faultInstanceStruct *)sf_get_chart_instance_ptr(S);
    if (ssIsFirstInitCond(S)) {
      /* do this only if simulation is starting and after we know the addresses of all data */
      {
        _SFD_SET_DATA_VALUE_PTR(4U, (void *)chartInstance->c3_u);
        _SFD_SET_DATA_VALUE_PTR(5U, (void *)chartInstance->c3_LO_mode);
        _SFD_SET_DATA_VALUE_PTR(6U, (void *)chartInstance->c3_RO_mode);
        _SFD_SET_DATA_VALUE_PTR(7U, (void *)chartInstance->c3_LI_mode);
        _SFD_SET_DATA_VALUE_PTR(8U, (void *)chartInstance->c3_RI_mode);
        _SFD_SET_DATA_VALUE_PTR(0U, (void *)&chartInstance->c3_fails);
        _SFD_SET_DATA_VALUE_PTR(1U, (void *)&chartInstance->c3_b_fails);
        _SFD_SET_DATA_VALUE_PTR(2U, (void *)&chartInstance->c3_c_fails);
        _SFD_SET_DATA_VALUE_PTR(3U, (void *)&chartInstance->c3_d_fails);
      }
    }
  }
}

static const char* sf_get_instance_specialization(void)
{
  return "s6yuDDe0R7K4Bbm7ZXEkuTC";
}

static void sf_opaque_initialize_c3_sf_aircraft_fault(void *chartInstanceVar)
{
  chart_debug_initialization(((SFc3_sf_aircraft_faultInstanceStruct*)
    chartInstanceVar)->S,0);
  initialize_params_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
    chartInstanceVar);
  initialize_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
    chartInstanceVar);
}

static void sf_opaque_enable_c3_sf_aircraft_fault(void *chartInstanceVar)
{
  enable_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
    chartInstanceVar);
}

static void sf_opaque_disable_c3_sf_aircraft_fault(void *chartInstanceVar)
{
  disable_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
    chartInstanceVar);
}

static void sf_opaque_gateway_c3_sf_aircraft_fault(void *chartInstanceVar)
{
  sf_gateway_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
    chartInstanceVar);
}

static const mxArray* sf_opaque_get_sim_state_c3_sf_aircraft_fault(SimStruct* S)
{
  return get_sim_state_c3_sf_aircraft_fault
    ((SFc3_sf_aircraft_faultInstanceStruct *)sf_get_chart_instance_ptr(S));/* raw sim ctx */
}

static void sf_opaque_set_sim_state_c3_sf_aircraft_fault(SimStruct* S, const
  mxArray *st)
{
  set_sim_state_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
    sf_get_chart_instance_ptr(S), st);
}

static void sf_opaque_terminate_c3_sf_aircraft_fault(void *chartInstanceVar)
{
  if (chartInstanceVar!=NULL) {
    SimStruct *S = ((SFc3_sf_aircraft_faultInstanceStruct*) chartInstanceVar)->S;
    if (sim_mode_is_rtw_gen(S) || sim_mode_is_external(S)) {
      sf_clear_rtw_identifier(S);
      unload_sf_aircraft_fault_optimization_info();
    }

    finalize_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
      chartInstanceVar);
    utFree(chartInstanceVar);
    if (ssGetUserData(S)!= NULL) {
      sf_free_ChartRunTimeInfo(S);
    }

    ssSetUserData(S,NULL);
  }
}

static void sf_opaque_init_subchart_simstructs(void *chartInstanceVar)
{
  initSimStructsc3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
    chartInstanceVar);
}

extern unsigned int sf_machine_global_initializer_called(void);
static void mdlProcessParameters_c3_sf_aircraft_fault(SimStruct *S)
{
  int i;
  for (i=0;i<ssGetNumRunTimeParams(S);i++) {
    if (ssGetSFcnParamTunable(S,i)) {
      ssUpdateDlgParamAsRunTimeParam(S,i);
    }
  }

  if (sf_machine_global_initializer_called()) {
    initialize_params_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
      sf_get_chart_instance_ptr(S));
  }
}

static void mdlSetWorkWidths_c3_sf_aircraft_fault(SimStruct *S)
{
  ssSetInputPortDirectFeedThrough(S, 0, 1);
  ssSetStatesModifiedOnlyInUpdate(S, 0);
  ssSetBlockIsPurelyCombinatorial_wrapper(S, 0);
  ssMdlUpdateIsEmpty(S, 1);
  if (sim_mode_is_rtw_gen(S) || sim_mode_is_external(S)) {
    mxArray *infoStruct = load_sf_aircraft_fault_optimization_info
      (sim_mode_is_rtw_gen(S), sim_mode_is_modelref_sim(S), sim_mode_is_external
       (S));
    int_T chartIsInlinable =
      (int_T)sf_is_chart_inlinable(sf_get_instance_specialization(),infoStruct,3);
    ssSetStateflowIsInlinable(S,chartIsInlinable);
    ssSetRTWCG(S,1);
    ssSetSupportedForRowMajorCodeGen(S, 1);
    ssSetEnableFcnIsTrivial(S,1);
    ssSetDisableFcnIsTrivial(S,1);
    ssSetNotMultipleInlinable(S,sf_rtw_info_uint_prop
      (sf_get_instance_specialization(),infoStruct,3,
       "gatewayCannotBeInlinedMultipleTimes"));
    sf_set_chart_accesses_machine_info(S, sf_get_instance_specialization(),
      infoStruct, 3);
    sf_update_buildInfo(S, sf_get_instance_specialization(),infoStruct,3);
    if (chartIsInlinable) {
      ssSetInputPortOptimOpts(S, 0, SS_REUSABLE_AND_LOCAL);
      sf_mark_chart_expressionable_inputs(S,sf_get_instance_specialization(),
        infoStruct,3,1);
      sf_mark_chart_reusable_outputs(S,sf_get_instance_specialization(),
        infoStruct,3,4);
    }

    {
      unsigned int outPortIdx;
      for (outPortIdx=1; outPortIdx<=4; ++outPortIdx) {
        ssSetOutputPortOptimizeInIR(S, outPortIdx, 1U);
      }
    }

    {
      unsigned int inPortIdx;
      for (inPortIdx=0; inPortIdx < 1; ++inPortIdx) {
        ssSetInputPortOptimizeInIR(S, inPortIdx, 1U);
      }
    }

    sf_set_rtw_dwork_info(S,sf_get_instance_specialization(),infoStruct,3);
    sf_register_codegen_names_for_scoped_functions_defined_by_chart(S);
    ssSetHasSubFunctions(S,!(chartIsInlinable));
  } else {
  }

  ssSetOptions(S,ssGetOptions(S)|SS_OPTION_WORKS_WITH_CODE_REUSE);
  ssSetChecksum0(S,(606899325U));
  ssSetChecksum1(S,(3588079688U));
  ssSetChecksum2(S,(1301307067U));
  ssSetChecksum3(S,(3621934660U));
  ssSetmdlDerivatives(S, NULL);
  ssSetExplicitFCSSCtrl(S,1);
  ssSetStateSemanticsClassicAndSynchronous(S, true);
  ssSupportsMultipleExecInstances(S,1);
}

static void mdlRTW_c3_sf_aircraft_fault(SimStruct *S)
{
  if (sim_mode_is_rtw_gen(S)) {
    ssWriteRTWStrParam(S, "StateflowChartType", "Stateflow");
  }
}

static void mdlStart_c3_sf_aircraft_fault(SimStruct *S)
{
  SFc3_sf_aircraft_faultInstanceStruct *chartInstance;
  chartInstance = (SFc3_sf_aircraft_faultInstanceStruct *)utMalloc(sizeof
    (SFc3_sf_aircraft_faultInstanceStruct));
  if (chartInstance==NULL) {
    sf_mex_error_message("Could not allocate memory for chart instance.");
  }

  memset(chartInstance, 0, sizeof(SFc3_sf_aircraft_faultInstanceStruct));
  chartInstance->chartInfo.chartInstance = chartInstance;
  chartInstance->chartInfo.isEMLChart = 0;
  chartInstance->chartInfo.chartInitialized = 0;
  chartInstance->chartInfo.sFunctionGateway =
    sf_opaque_gateway_c3_sf_aircraft_fault;
  chartInstance->chartInfo.initializeChart =
    sf_opaque_initialize_c3_sf_aircraft_fault;
  chartInstance->chartInfo.terminateChart =
    sf_opaque_terminate_c3_sf_aircraft_fault;
  chartInstance->chartInfo.enableChart = sf_opaque_enable_c3_sf_aircraft_fault;
  chartInstance->chartInfo.disableChart = sf_opaque_disable_c3_sf_aircraft_fault;
  chartInstance->chartInfo.getSimState =
    sf_opaque_get_sim_state_c3_sf_aircraft_fault;
  chartInstance->chartInfo.setSimState =
    sf_opaque_set_sim_state_c3_sf_aircraft_fault;
  chartInstance->chartInfo.getSimStateInfo =
    sf_get_sim_state_info_c3_sf_aircraft_fault;
  chartInstance->chartInfo.zeroCrossings = NULL;
  chartInstance->chartInfo.outputs = NULL;
  chartInstance->chartInfo.derivatives = NULL;
  chartInstance->chartInfo.mdlRTW = mdlRTW_c3_sf_aircraft_fault;
  chartInstance->chartInfo.mdlStart = mdlStart_c3_sf_aircraft_fault;
  chartInstance->chartInfo.mdlSetWorkWidths =
    mdlSetWorkWidths_c3_sf_aircraft_fault;
  chartInstance->chartInfo.callGetHoverDataForMsg =
    sf_opaque_get_hover_data_for_msg;
  chartInstance->chartInfo.extModeExec = NULL;
  chartInstance->chartInfo.restoreLastMajorStepConfiguration = NULL;
  chartInstance->chartInfo.restoreBeforeLastMajorStepConfiguration = NULL;
  chartInstance->chartInfo.storeCurrentConfiguration = NULL;
  chartInstance->chartInfo.callAtomicSubchartUserFcn = NULL;
  chartInstance->chartInfo.callAtomicSubchartAutoFcn = NULL;
  chartInstance->chartInfo.callAtomicSubchartEventFcn = NULL;
  chartInstance->chartInfo.debugInstance = sfGlobalDebugInstanceStruct;
  chartInstance->S = S;
  sf_init_ChartRunTimeInfo(S, &(chartInstance->chartInfo), false, 0);
  init_dsm_address_info(chartInstance);
  init_simulink_io_address(chartInstance);
  if (!sim_mode_is_rtw_gen(S)) {
  }

  chart_debug_initialization(S,1);
  mdl_start_c3_sf_aircraft_fault(chartInstance);
}

void c3_sf_aircraft_fault_method_dispatcher(SimStruct *S, int_T method, void
  *data)
{
  switch (method) {
   case SS_CALL_MDL_START:
    mdlStart_c3_sf_aircraft_fault(S);
    break;

   case SS_CALL_MDL_SET_WORK_WIDTHS:
    mdlSetWorkWidths_c3_sf_aircraft_fault(S);
    break;

   case SS_CALL_MDL_PROCESS_PARAMETERS:
    mdlProcessParameters_c3_sf_aircraft_fault(S);
    break;

   default:
    /* Unhandled method */
    sf_mex_error_message("Stateflow Internal Error:\n"
                         "Error calling c3_sf_aircraft_fault_method_dispatcher.\n"
                         "Can't handle method %d.\n", method);
    break;
  }
}
