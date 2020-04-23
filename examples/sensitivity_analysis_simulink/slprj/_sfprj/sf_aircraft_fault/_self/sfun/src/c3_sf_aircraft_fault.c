/* Include files */

#include "sf_aircraft_fault_sfun.h"
#include "c3_sf_aircraft_fault.h"
#define _SF_MEX_LISTEN_FOR_CTRL_C(S)   sf_mex_listen_for_ctrl_c(S);
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
static const char * c3_sv[5] = { "Isolated", "Off", "Passive", "Standby",
  "Active" };

static const int32_T c3_iv[5] = { 0, 1, 2, 3, 4 };

/* Function Declarations */
static void initialize_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void initialize_params_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void enable_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void disable_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void c3_update_jit_animation_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_do_animation_call_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void ext_mode_exec_c3_sf_aircraft_fault
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
static void c3_L_switch(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_R_switch(SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static sf_aircraft_ModeType c3_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray
   *c3_b_LI_mode, const char_T *c3_identifier);
static sf_aircraft_ModeType c3_b_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray *c3_b_u,
   const emlrtMsgIdentifier *c3_parentId);
static int32_T c3_c_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_e_fails, const char_T *c3_identifier);
static int32_T c3_d_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static uint8_T c3_e_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_is_active_c3_sf_aircraft_fault, const
  char_T *c3_identifier);
static uint8_T c3_f_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static const mxArray *c3_g_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_setSimStateSideEffectsInfo, const char_T
  *c3_identifier);
static const mxArray *c3_h_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId);
static void c3_slStringInitializeDynamicBuffers
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance);
static void c3_init_sf_message_store_memory(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static const mxArray *c3_chart_data_browse_helper
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, int32_T c3_ssIdNumber);
static int32_T c3__s32_add__(SFc3_sf_aircraft_faultInstanceStruct *chartInstance,
  int32_T c3_b, int32_T c3_c, int32_T c3_EMLOvCount_src_loc, uint32_T
  c3_ssid_src_loc, int32_T c3_offset_src_loc, int32_T c3_length_src_loc);
static void init_dsm_address_info(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);
static void init_simulink_io_address(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance);

/* Function Definitions */
static void initialize_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  sim_mode_is_external(chartInstance->S);
  chartInstance->c3_sfEvent = CALL_EVENT;
  _sfTime_ = sf_get_time(chartInstance->S);
  chartInstance->c3_doSetSimStateSideEffects = 0U;
  chartInstance->c3_setSimStateSideEffectsInfo = NULL;
  chartInstance->c3_is_active_LI = 0U;
  chartInstance->c3_is_LI = c3_IN_NO_ACTIVE_CHILD;
  *chartInstance->c3_LI_mode = Isolated;
  chartInstance->c3_is_active_LO = 0U;
  chartInstance->c3_is_LO = c3_IN_NO_ACTIVE_CHILD;
  *chartInstance->c3_LO_mode = Isolated;
  chartInstance->c3_is_active_RI = 0U;
  chartInstance->c3_is_RI = c3_IN_NO_ACTIVE_CHILD;
  *chartInstance->c3_RI_mode = Isolated;
  chartInstance->c3_is_active_RO = 0U;
  chartInstance->c3_is_RO = c3_IN_NO_ACTIVE_CHILD;
  *chartInstance->c3_RO_mode = Isolated;
  chartInstance->c3_is_active_c3_sf_aircraft_fault = 0U;
  chartInstance->c3_is_c3_sf_aircraft_fault = c3_IN_NO_ACTIVE_CHILD;
  chartInstance->c3_fails = 0;
  chartInstance->c3_b_fails = 0;
  chartInstance->c3_c_fails = 0;
  chartInstance->c3_d_fails = 0;
  if (sf_get_output_port_reusable(chartInstance->S, 1) == 0) {
    *chartInstance->c3_LO_mode = Isolated;
  }

  if (sf_get_output_port_reusable(chartInstance->S, 2) == 0) {
    *chartInstance->c3_RO_mode = Isolated;
  }

  if (sf_get_output_port_reusable(chartInstance->S, 3) == 0) {
    *chartInstance->c3_LI_mode = Isolated;
  }

  if (sf_get_output_port_reusable(chartInstance->S, 4) == 0) {
    *chartInstance->c3_RI_mode = Isolated;
  }

  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 0U, (real_T)
                    chartInstance->c3_fails);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 1U, (real_T)
                    chartInstance->c3_b_fails);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 2U, (real_T)
                    chartInstance->c3_c_fails);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 3U, (real_T)
                    chartInstance->c3_d_fails);
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

static void c3_update_jit_animation_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  chartInstance->c3_JITStateAnimation[0U] = (uint8_T)
    (chartInstance->c3_is_c3_sf_aircraft_fault == c3_IN_Actuators);
  chartInstance->c3_JITStateAnimation[1U] = (uint8_T)
    (chartInstance->c3_is_active_LO == 1U);
  chartInstance->c3_JITStateAnimation[2U] = (uint8_T)(chartInstance->c3_is_LO ==
    c3_IN_L1);
  chartInstance->c3_JITStateAnimation[3U] = (uint8_T)(*chartInstance->c3_LO_mode
    == Passive);
  chartInstance->c3_JITStateAnimation[4U] = (uint8_T)(*chartInstance->c3_LO_mode
    == Active);
  chartInstance->c3_JITStateAnimation[5U] = (uint8_T)(*chartInstance->c3_LO_mode
    == Standby);
  chartInstance->c3_JITStateAnimation[6U] = (uint8_T)(chartInstance->c3_is_LO ==
    c3_IN_Isolated);
  chartInstance->c3_JITStateAnimation[7U] = (uint8_T)
    (chartInstance->c3_is_active_RO == 1U);
  chartInstance->c3_JITStateAnimation[8U] = (uint8_T)(chartInstance->c3_is_RO ==
    c3_IN_L1);
  chartInstance->c3_JITStateAnimation[9U] = (uint8_T)(*chartInstance->c3_RO_mode
    == Passive);
  chartInstance->c3_JITStateAnimation[10U] = (uint8_T)
    (*chartInstance->c3_RO_mode == Active);
  chartInstance->c3_JITStateAnimation[11U] = (uint8_T)
    (*chartInstance->c3_RO_mode == Standby);
  chartInstance->c3_JITStateAnimation[12U] = (uint8_T)
    (*chartInstance->c3_RO_mode == Off);
  chartInstance->c3_JITStateAnimation[13U] = (uint8_T)(chartInstance->c3_is_RO ==
    c3_IN_Isolated);
  chartInstance->c3_JITStateAnimation[14U] = (uint8_T)
    (chartInstance->c3_is_active_LI == 1U);
  chartInstance->c3_JITStateAnimation[15U] = (uint8_T)(chartInstance->c3_is_LI ==
    c3_IN_L1);
  chartInstance->c3_JITStateAnimation[16U] = (uint8_T)
    (*chartInstance->c3_LI_mode == Passive);
  chartInstance->c3_JITStateAnimation[17U] = (uint8_T)
    (*chartInstance->c3_LI_mode == Active);
  chartInstance->c3_JITStateAnimation[18U] = (uint8_T)
    (*chartInstance->c3_LI_mode == Standby);
  chartInstance->c3_JITStateAnimation[19U] = (uint8_T)
    (*chartInstance->c3_LI_mode == Off);
  chartInstance->c3_JITStateAnimation[20U] = (uint8_T)(chartInstance->c3_is_LI ==
    c3_IN_Isolated);
  chartInstance->c3_JITStateAnimation[21U] = (uint8_T)
    (chartInstance->c3_is_active_RI == 1U);
  chartInstance->c3_JITStateAnimation[22U] = (uint8_T)(chartInstance->c3_is_RI ==
    c3_IN_L1);
  chartInstance->c3_JITStateAnimation[23U] = (uint8_T)
    (*chartInstance->c3_RI_mode == Passive);
  chartInstance->c3_JITStateAnimation[24U] = (uint8_T)
    (*chartInstance->c3_RI_mode == Active);
  chartInstance->c3_JITStateAnimation[25U] = (uint8_T)
    (*chartInstance->c3_RI_mode == Standby);
  chartInstance->c3_JITStateAnimation[26U] = (uint8_T)
    (*chartInstance->c3_RI_mode == Off);
  chartInstance->c3_JITStateAnimation[27U] = (uint8_T)(chartInstance->c3_is_RI ==
    c3_IN_Isolated);
  chartInstance->c3_JITStateAnimation[28U] = (uint8_T)
    (*chartInstance->c3_LO_mode == Off);
}

static void c3_do_animation_call_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  sfDoAnimationWrapper(chartInstance->S, false, true);
  sfDoAnimationWrapper(chartInstance->S, false, false);
}

static void ext_mode_exec_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static const mxArray *get_sim_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  const mxArray *c3_st;
  const mxArray *c3_y = NULL;
  const mxArray *c3_b_y = NULL;
  int32_T c3_b_u;
  const mxArray *c3_c_y = NULL;
  const mxArray *c3_m = NULL;
  const mxArray *c3_d_y = NULL;
  int32_T c3_c_u;
  const mxArray *c3_e_y = NULL;
  const mxArray *c3_m1 = NULL;
  const mxArray *c3_f_y = NULL;
  int32_T c3_d_u;
  const mxArray *c3_g_y = NULL;
  const mxArray *c3_m2 = NULL;
  const mxArray *c3_h_y = NULL;
  int32_T c3_e_u;
  const mxArray *c3_i_y = NULL;
  const mxArray *c3_m3 = NULL;
  const mxArray *c3_j_y = NULL;
  const mxArray *c3_k_y = NULL;
  const mxArray *c3_l_y = NULL;
  const mxArray *c3_m_y = NULL;
  const mxArray *c3_n_y = NULL;
  const mxArray *c3_o_y = NULL;
  const mxArray *c3_p_y = NULL;
  const mxArray *c3_q_y = NULL;
  const mxArray *c3_r_y = NULL;
  const mxArray *c3_s_y = NULL;
  const mxArray *c3_t_y = NULL;
  const mxArray *c3_u_y = NULL;
  const mxArray *c3_v_y = NULL;
  const mxArray *c3_w_y = NULL;
  c3_st = NULL;
  c3_st = NULL;
  c3_y = NULL;
  sf_mex_assign(&c3_y, sf_mex_createcellmatrix(18, 1), false);
  c3_b_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv, c3_iv);
  c3_b_u = (int32_T)*chartInstance->c3_LI_mode;
  c3_c_y = NULL;
  sf_mex_assign(&c3_c_y, sf_mex_create("y", &c3_b_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m, c3_c_y, false);
  sf_mex_assign(&c3_b_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m), false);
  sf_mex_destroy(&c3_m);
  sf_mex_setcell(c3_y, 0, c3_b_y);
  c3_d_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv, c3_iv);
  c3_c_u = (int32_T)*chartInstance->c3_LO_mode;
  c3_e_y = NULL;
  sf_mex_assign(&c3_e_y, sf_mex_create("y", &c3_c_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m1, c3_e_y, false);
  sf_mex_assign(&c3_d_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m1),
                false);
  sf_mex_destroy(&c3_m1);
  sf_mex_setcell(c3_y, 1, c3_d_y);
  c3_f_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv, c3_iv);
  c3_d_u = (int32_T)*chartInstance->c3_RI_mode;
  c3_g_y = NULL;
  sf_mex_assign(&c3_g_y, sf_mex_create("y", &c3_d_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m2, c3_g_y, false);
  sf_mex_assign(&c3_f_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m2),
                false);
  sf_mex_destroy(&c3_m2);
  sf_mex_setcell(c3_y, 2, c3_f_y);
  c3_h_y = NULL;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv, c3_iv);
  c3_e_u = (int32_T)*chartInstance->c3_RO_mode;
  c3_i_y = NULL;
  sf_mex_assign(&c3_i_y, sf_mex_create("y", &c3_e_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c3_m3, c3_i_y, false);
  sf_mex_assign(&c3_h_y, sf_mex_create_enum("sf_aircraft_ModeType", c3_m3),
                false);
  sf_mex_destroy(&c3_m3);
  sf_mex_setcell(c3_y, 3, c3_h_y);
  c3_j_y = NULL;
  sf_mex_assign(&c3_j_y, sf_mex_create("y", &chartInstance->c3_fails, 6, 0U, 0U,
    0U, 0), false);
  sf_mex_setcell(c3_y, 4, c3_j_y);
  c3_k_y = NULL;
  sf_mex_assign(&c3_k_y, sf_mex_create("y", &chartInstance->c3_b_fails, 6, 0U,
    0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 5, c3_k_y);
  c3_l_y = NULL;
  sf_mex_assign(&c3_l_y, sf_mex_create("y", &chartInstance->c3_c_fails, 6, 0U,
    0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 6, c3_l_y);
  c3_m_y = NULL;
  sf_mex_assign(&c3_m_y, sf_mex_create("y", &chartInstance->c3_d_fails, 6, 0U,
    0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 7, c3_m_y);
  c3_n_y = NULL;
  sf_mex_assign(&c3_n_y, sf_mex_create("y",
    &chartInstance->c3_is_active_c3_sf_aircraft_fault, 3, 0U, 0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 8, c3_n_y);
  c3_o_y = NULL;
  sf_mex_assign(&c3_o_y, sf_mex_create("y", &chartInstance->c3_is_active_LO, 3,
    0U, 0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 9, c3_o_y);
  c3_p_y = NULL;
  sf_mex_assign(&c3_p_y, sf_mex_create("y", &chartInstance->c3_is_active_RO, 3,
    0U, 0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 10, c3_p_y);
  c3_q_y = NULL;
  sf_mex_assign(&c3_q_y, sf_mex_create("y", &chartInstance->c3_is_active_LI, 3,
    0U, 0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 11, c3_q_y);
  c3_r_y = NULL;
  sf_mex_assign(&c3_r_y, sf_mex_create("y", &chartInstance->c3_is_active_RI, 3,
    0U, 0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 12, c3_r_y);
  c3_s_y = NULL;
  sf_mex_assign(&c3_s_y, sf_mex_create("y",
    &chartInstance->c3_is_c3_sf_aircraft_fault, 3, 0U, 0U, 0U, 0), false);
  sf_mex_setcell(c3_y, 13, c3_s_y);
  c3_t_y = NULL;
  sf_mex_assign(&c3_t_y, sf_mex_create("y", &chartInstance->c3_is_LO, 3, 0U, 0U,
    0U, 0), false);
  sf_mex_setcell(c3_y, 14, c3_t_y);
  c3_u_y = NULL;
  sf_mex_assign(&c3_u_y, sf_mex_create("y", &chartInstance->c3_is_RO, 3, 0U, 0U,
    0U, 0), false);
  sf_mex_setcell(c3_y, 15, c3_u_y);
  c3_v_y = NULL;
  sf_mex_assign(&c3_v_y, sf_mex_create("y", &chartInstance->c3_is_LI, 3, 0U, 0U,
    0U, 0), false);
  sf_mex_setcell(c3_y, 16, c3_v_y);
  c3_w_y = NULL;
  sf_mex_assign(&c3_w_y, sf_mex_create("y", &chartInstance->c3_is_RI, 3, 0U, 0U,
    0U, 0), false);
  sf_mex_setcell(c3_y, 17, c3_w_y);
  sf_mex_assign(&c3_st, c3_y, false);
  return c3_st;
}

static void set_sim_state_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray *c3_st)
{
  const mxArray *c3_b_u;
  c3_b_u = sf_mex_dup(c3_st);
  *chartInstance->c3_LI_mode = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 0)), "LI_mode");
  *chartInstance->c3_LO_mode = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 1)), "LO_mode");
  *chartInstance->c3_RI_mode = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 2)), "RI_mode");
  *chartInstance->c3_RO_mode = c3_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 3)), "RO_mode");
  chartInstance->c3_fails = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 4)), "fails");
  chartInstance->c3_b_fails = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 5)), "fails");
  chartInstance->c3_c_fails = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 6)), "fails");
  chartInstance->c3_d_fails = c3_c_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 7)), "fails");
  chartInstance->c3_is_active_c3_sf_aircraft_fault = c3_e_emlrt_marshallIn
    (chartInstance, sf_mex_dup(sf_mex_getcell(c3_b_u, 8)),
     "is_active_c3_sf_aircraft_fault");
  chartInstance->c3_is_active_LO = c3_e_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 9)), "is_active_LO");
  chartInstance->c3_is_active_RO = c3_e_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 10)), "is_active_RO");
  chartInstance->c3_is_active_LI = c3_e_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 11)), "is_active_LI");
  chartInstance->c3_is_active_RI = c3_e_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell(c3_b_u, 12)), "is_active_RI");
  chartInstance->c3_is_c3_sf_aircraft_fault = c3_e_emlrt_marshallIn
    (chartInstance, sf_mex_dup(sf_mex_getcell(c3_b_u, 13)),
     "is_c3_sf_aircraft_fault");
  chartInstance->c3_is_LO = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 14)), "is_LO");
  chartInstance->c3_is_RO = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 15)), "is_RO");
  chartInstance->c3_is_LI = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 16)), "is_LI");
  chartInstance->c3_is_RI = c3_e_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell(c3_b_u, 17)), "is_RI");
  sf_mex_assign(&chartInstance->c3_setSimStateSideEffectsInfo,
                c3_g_emlrt_marshallIn(chartInstance, sf_mex_dup(sf_mex_getcell
    (c3_b_u, 18)), "setSimStateSideEffectsInfo"), true);
  sf_mex_destroy(&c3_b_u);
  chartInstance->c3_doSetSimStateSideEffects = 1U;
  c3_update_jit_animation_state_c3_sf_aircraft_fault(chartInstance);
  sf_mex_destroy(&c3_st);
}

static void c3_set_sim_state_side_effects_c3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  if (chartInstance->c3_doSetSimStateSideEffects != 0) {
    chartInstance->c3_doSetSimStateSideEffects = 0U;
  }
}

static void finalize_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  sfListenerLightTerminate(chartInstance->c3_RuntimeVar);
  sf_mex_destroy(&chartInstance->c3_setSimStateSideEffectsInfo);
  covrtDeleteStateflowInstanceData(chartInstance->c3_covrtInstance);
}

static void sf_gateway_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  c3_set_sim_state_side_effects_c3_sf_aircraft_fault(chartInstance);
  chartInstance->c3_JITTransitionAnimation[0] = 0U;
  chartInstance->c3_JITTransitionAnimation[1] = 0U;
  chartInstance->c3_JITTransitionAnimation[2] = 0U;
  chartInstance->c3_JITTransitionAnimation[3] = 0U;
  chartInstance->c3_JITTransitionAnimation[4] = 0U;
  chartInstance->c3_JITTransitionAnimation[5] = 0U;
  chartInstance->c3_JITTransitionAnimation[6] = 0U;
  chartInstance->c3_JITTransitionAnimation[7] = 0U;
  chartInstance->c3_JITTransitionAnimation[8] = 0U;
  chartInstance->c3_JITTransitionAnimation[9] = 0U;
  chartInstance->c3_JITTransitionAnimation[10] = 0U;
  chartInstance->c3_JITTransitionAnimation[11] = 0U;
  chartInstance->c3_JITTransitionAnimation[12] = 0U;
  chartInstance->c3_JITTransitionAnimation[13] = 0U;
  chartInstance->c3_JITTransitionAnimation[14] = 0U;
  chartInstance->c3_JITTransitionAnimation[15] = 0U;
  chartInstance->c3_JITTransitionAnimation[16] = 0U;
  chartInstance->c3_JITTransitionAnimation[17] = 0U;
  chartInstance->c3_JITTransitionAnimation[18] = 0U;
  chartInstance->c3_JITTransitionAnimation[19] = 0U;
  chartInstance->c3_JITTransitionAnimation[20] = 0U;
  chartInstance->c3_JITTransitionAnimation[21] = 0U;
  chartInstance->c3_JITTransitionAnimation[22] = 0U;
  chartInstance->c3_JITTransitionAnimation[23] = 0U;
  chartInstance->c3_JITTransitionAnimation[24] = 0U;
  chartInstance->c3_JITTransitionAnimation[25] = 0U;
  chartInstance->c3_JITTransitionAnimation[26] = 0U;
  chartInstance->c3_JITTransitionAnimation[27] = 0U;
  chartInstance->c3_JITTransitionAnimation[28] = 0U;
  chartInstance->c3_JITTransitionAnimation[29] = 0U;
  chartInstance->c3_JITTransitionAnimation[30] = 0U;
  chartInstance->c3_JITTransitionAnimation[31] = 0U;
  chartInstance->c3_JITTransitionAnimation[32] = 0U;
  chartInstance->c3_JITTransitionAnimation[33] = 0U;
  chartInstance->c3_JITTransitionAnimation[34] = 0U;
  chartInstance->c3_JITTransitionAnimation[35] = 0U;
  chartInstance->c3_JITTransitionAnimation[36] = 0U;
  chartInstance->c3_JITTransitionAnimation[37] = 0U;
  chartInstance->c3_JITTransitionAnimation[38] = 0U;
  chartInstance->c3_JITTransitionAnimation[39] = 0U;
  chartInstance->c3_JITTransitionAnimation[40] = 0U;
  chartInstance->c3_JITTransitionAnimation[41] = 0U;
  chartInstance->c3_JITTransitionAnimation[42] = 0U;
  chartInstance->c3_JITTransitionAnimation[43] = 0U;
  chartInstance->c3_JITTransitionAnimation[44] = 0U;
  chartInstance->c3_JITTransitionAnimation[45] = 0U;
  chartInstance->c3_JITTransitionAnimation[46] = 0U;
  chartInstance->c3_JITTransitionAnimation[47] = 0U;
  chartInstance->c3_JITTransitionAnimation[48] = 0U;
  chartInstance->c3_JITTransitionAnimation[49] = 0U;
  chartInstance->c3_JITTransitionAnimation[50] = 0U;
  chartInstance->c3_JITTransitionAnimation[51] = 0U;
  chartInstance->c3_JITTransitionAnimation[52] = 0U;
  chartInstance->c3_JITTransitionAnimation[53] = 0U;
  chartInstance->c3_JITTransitionAnimation[54] = 0U;
  chartInstance->c3_JITTransitionAnimation[55] = 0U;
  chartInstance->c3_JITTransitionAnimation[56] = 0U;
  chartInstance->c3_JITTransitionAnimation[57] = 0U;
  chartInstance->c3_JITTransitionAnimation[58] = 0U;
  chartInstance->c3_JITTransitionAnimation[59] = 0U;
  chartInstance->c3_JITTransitionAnimation[60] = 0U;
  chartInstance->c3_JITTransitionAnimation[61] = 0U;
  chartInstance->c3_JITTransitionAnimation[62] = 0U;
  chartInstance->c3_JITTransitionAnimation[63] = 0U;
  chartInstance->c3_JITTransitionAnimation[64] = 0U;
  chartInstance->c3_JITTransitionAnimation[65] = 0U;
  chartInstance->c3_JITTransitionAnimation[66] = 0U;
  chartInstance->c3_JITTransitionAnimation[67] = 0U;
  chartInstance->c3_JITTransitionAnimation[68] = 0U;
  chartInstance->c3_JITTransitionAnimation[69] = 0U;
  chartInstance->c3_JITTransitionAnimation[70] = 0U;
  chartInstance->c3_JITTransitionAnimation[71] = 0U;
  chartInstance->c3_JITTransitionAnimation[72] = 0U;
  chartInstance->c3_JITTransitionAnimation[73] = 0U;
  chartInstance->c3_JITTransitionAnimation[74] = 0U;
  chartInstance->c3_JITTransitionAnimation[75] = 0U;
  chartInstance->c3_JITTransitionAnimation[76] = 0U;
  chartInstance->c3_JITTransitionAnimation[77] = 0U;
  chartInstance->c3_JITTransitionAnimation[78] = 0U;
  chartInstance->c3_JITTransitionAnimation[79] = 0U;
  chartInstance->c3_JITTransitionAnimation[80] = 0U;
  chartInstance->c3_JITTransitionAnimation[81] = 0U;
  chartInstance->c3_JITTransitionAnimation[82] = 0U;
  chartInstance->c3_JITTransitionAnimation[83] = 0U;
  chartInstance->c3_JITTransitionAnimation[84] = 0U;
  chartInstance->c3_JITTransitionAnimation[85] = 0U;
  chartInstance->c3_JITTransitionAnimation[86] = 0U;
  chartInstance->c3_JITTransitionAnimation[87] = 0U;
  chartInstance->c3_JITTransitionAnimation[88] = 0U;
  chartInstance->c3_JITTransitionAnimation[89] = 0U;
  chartInstance->c3_JITTransitionAnimation[90] = 0U;
  chartInstance->c3_JITTransitionAnimation[91] = 0U;
  chartInstance->c3_JITTransitionAnimation[92] = 0U;
  chartInstance->c3_JITTransitionAnimation[93] = 0U;
  chartInstance->c3_JITTransitionAnimation[94] = 0U;
  chartInstance->c3_JITTransitionAnimation[95] = 0U;
  chartInstance->c3_JITTransitionAnimation[96] = 0U;
  chartInstance->c3_JITTransitionAnimation[97] = 0U;
  chartInstance->c3_JITTransitionAnimation[98] = 0U;
  chartInstance->c3_JITTransitionAnimation[99] = 0U;
  chartInstance->c3_JITTransitionAnimation[100] = 0U;
  chartInstance->c3_JITTransitionAnimation[101] = 0U;
  chartInstance->c3_JITTransitionAnimation[102] = 0U;
  chartInstance->c3_JITTransitionAnimation[103] = 0U;
  _sfTime_ = sf_get_time(chartInstance->S);
  chartInstance->c3_sfEvent = CALL_EVENT;
  if (chartInstance->c3_is_active_c3_sf_aircraft_fault == 0U) {
    chartInstance->c3_is_active_c3_sf_aircraft_fault = 1U;
    chartInstance->c3_is_c3_sf_aircraft_fault = c3_IN_Actuators;
    c3_L_switch(chartInstance);
    c3_R_switch(chartInstance);
    chartInstance->c3_is_active_LO = 1U;
    chartInstance->c3_fails = 0;
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 0U, (real_T)
                      chartInstance->c3_fails);
    chartInstance->c3_JITTransitionAnimation[10U] = 1U;
    chartInstance->c3_is_LO = c3_IN_L1;
    chartInstance->c3_JITTransitionAnimation[15U] = 1U;
    *chartInstance->c3_LO_mode = Passive;
    chartInstance->c3_is_active_RO = 1U;
    chartInstance->c3_b_fails = 0;
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 1U, (real_T)
                      chartInstance->c3_b_fails);
    chartInstance->c3_JITTransitionAnimation[47U] = 1U;
    chartInstance->c3_is_RO = c3_IN_L1;
    chartInstance->c3_JITTransitionAnimation[50U] = 1U;
    *chartInstance->c3_RO_mode = Passive;
    chartInstance->c3_is_active_LI = 1U;
    chartInstance->c3_c_fails = 0;
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 2U, (real_T)
                      chartInstance->c3_c_fails);
    chartInstance->c3_JITTransitionAnimation[5U] = 1U;
    chartInstance->c3_is_LI = c3_IN_L1;
    chartInstance->c3_JITTransitionAnimation[1U] = 1U;
    *chartInstance->c3_LI_mode = Passive;
    chartInstance->c3_is_active_RI = 1U;
    chartInstance->c3_d_fails = 0;
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 3U, (real_T)
                      chartInstance->c3_d_fails);
    chartInstance->c3_JITTransitionAnimation[38U] = 1U;
    chartInstance->c3_is_RI = c3_IN_L1;
    chartInstance->c3_JITTransitionAnimation[35U] = 1U;
    *chartInstance->c3_RI_mode = Passive;
    if ((chartInstance->c3_is_active_c3_sf_aircraft_fault == 1U) &&
        (!(chartInstance->c3_is_c3_sf_aircraft_fault == c3_IN_Actuators))) {
      sf_state_inconsistency_error(chartInstance->S, 0);
    }
  } else {
    if (chartInstance->c3_is_c3_sf_aircraft_fault == c3_IN_Actuators) {
      c3_L_switch(chartInstance);
      c3_R_switch(chartInstance);
      if (chartInstance->c3_is_active_LO != 0U) {
        c3_LO(chartInstance);
      }

      if (chartInstance->c3_is_active_RO != 0U) {
        c3_RO(chartInstance);
      }

      if (chartInstance->c3_is_active_LI != 0U) {
        c3_LI(chartInstance);
      }

      if (chartInstance->c3_is_active_RI != 0U) {
        c3_RI(chartInstance);
      }
    }
  }

  c3_update_jit_animation_state_c3_sf_aircraft_fault(chartInstance);
  c3_do_animation_call_c3_sf_aircraft_fault(chartInstance);
}

static void mdl_start_c3_sf_aircraft_fault(SFc3_sf_aircraft_faultInstanceStruct *
  chartInstance)
{
  static const uint32_T c3_decisionTxtStartIdx = 0U;
  static const uint32_T c3_decisionTxtEndIdx = 0U;
  static const uint32_T c3_b_decisionTxtStartIdx = 0U;
  static const uint32_T c3_b_decisionTxtEndIdx = 0U;
  static const uint32_T c3_c_decisionTxtStartIdx = 0U;
  static const uint32_T c3_c_decisionTxtEndIdx = 0U;
  static const uint32_T c3_d_decisionTxtStartIdx = 0U;
  static const uint32_T c3_d_decisionTxtEndIdx = 0U;
  static const uint32_T c3_e_decisionTxtStartIdx = 0U;
  static const uint32_T c3_e_decisionTxtEndIdx = 0U;
  static const uint32_T c3_f_decisionTxtStartIdx = 0U;
  static const uint32_T c3_f_decisionTxtEndIdx = 0U;
  static const uint32_T c3_g_decisionTxtStartIdx = 0U;
  static const uint32_T c3_g_decisionTxtEndIdx = 0U;
  static const uint32_T c3_h_decisionTxtStartIdx = 0U;
  static const uint32_T c3_h_decisionTxtEndIdx = 0U;
  static const uint32_T c3_i_decisionTxtStartIdx = 0U;
  static const uint32_T c3_i_decisionTxtEndIdx = 0U;
  static const uint32_T c3_j_decisionTxtStartIdx = 0U;
  static const uint32_T c3_j_decisionTxtEndIdx = 0U;
  static const uint32_T c3_k_decisionTxtStartIdx = 0U;
  static const uint32_T c3_k_decisionTxtEndIdx = 0U;
  static const uint32_T c3_l_decisionTxtStartIdx = 0U;
  static const uint32_T c3_l_decisionTxtEndIdx = 0U;
  static const uint32_T c3_m_decisionTxtStartIdx = 0U;
  static const uint32_T c3_m_decisionTxtEndIdx = 0U;
  static const uint32_T c3_n_decisionTxtStartIdx = 0U;
  static const uint32_T c3_n_decisionTxtEndIdx = 0U;
  static const uint32_T c3_o_decisionTxtStartIdx = 0U;
  static const uint32_T c3_o_decisionTxtEndIdx = 0U;
  static const uint32_T c3_p_decisionTxtStartIdx = 0U;
  static const uint32_T c3_p_decisionTxtEndIdx = 0U;
  static const uint32_T c3_q_decisionTxtStartIdx = 0U;
  static const uint32_T c3_q_decisionTxtEndIdx = 0U;
  static const uint32_T c3_r_decisionTxtStartIdx = 0U;
  static const uint32_T c3_r_decisionTxtEndIdx = 0U;
  static const uint32_T c3_s_decisionTxtStartIdx = 0U;
  static const uint32_T c3_s_decisionTxtEndIdx = 0U;
  static const uint32_T c3_t_decisionTxtStartIdx = 0U;
  static const uint32_T c3_t_decisionTxtEndIdx = 0U;
  static const uint32_T c3_u_decisionTxtStartIdx = 0U;
  static const uint32_T c3_u_decisionTxtEndIdx = 0U;
  static const uint32_T c3_v_decisionTxtStartIdx = 0U;
  static const uint32_T c3_v_decisionTxtEndIdx = 0U;
  static const uint32_T c3_w_decisionTxtStartIdx = 0U;
  static const uint32_T c3_w_decisionTxtEndIdx = 0U;
  static const uint32_T c3_x_decisionTxtStartIdx = 0U;
  static const uint32_T c3_x_decisionTxtEndIdx = 0U;
  static const uint32_T c3_y_decisionTxtStartIdx = 0U;
  static const uint32_T c3_y_decisionTxtEndIdx = 0U;
  static const uint32_T c3_ab_decisionTxtStartIdx = 0U;
  static const uint32_T c3_ab_decisionTxtEndIdx = 0U;
  static const uint32_T c3_bb_decisionTxtStartIdx = 0U;
  static const uint32_T c3_bb_decisionTxtEndIdx = 0U;
  static const uint32_T c3_cb_decisionTxtStartIdx = 0U;
  static const uint32_T c3_cb_decisionTxtEndIdx = 0U;
  static const uint32_T c3_db_decisionTxtStartIdx = 0U;
  static const uint32_T c3_db_decisionTxtEndIdx = 0U;
  static const uint32_T c3_eb_decisionTxtStartIdx = 0U;
  static const uint32_T c3_eb_decisionTxtEndIdx = 0U;
  static const uint32_T c3_fb_decisionTxtStartIdx = 0U;
  static const uint32_T c3_fb_decisionTxtEndIdx = 0U;
  static const uint32_T c3_gb_decisionTxtStartIdx = 0U;
  static const uint32_T c3_gb_decisionTxtEndIdx = 0U;
  static const uint32_T c3_hb_decisionTxtStartIdx = 0U;
  static const uint32_T c3_hb_decisionTxtEndIdx = 0U;
  static const uint32_T c3_ib_decisionTxtStartIdx = 0U;
  static const uint32_T c3_ib_decisionTxtEndIdx = 0U;
  static const uint32_T c3_jb_decisionTxtStartIdx = 0U;
  static const uint32_T c3_jb_decisionTxtEndIdx = 0U;
  static const uint32_T c3_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_postfixPredicateTree[1] = { 0 };

  static const int32_T c3_relopTxtStartIdx[1] = { 1 };

  static const int32_T c3_relopTxtEndIdx[1] = { 9 };

  static const int32_T c3_relationalopEps[1] = { 0 };

  static const int32_T c3_relationalopType[1] = { 5 };

  static const uint32_T c3_b_transitionTxtStartIdx[1] = { 0U };

  static const uint32_T c3_b_transitionTxtEndIdx[1] = { 11U };

  static const int32_T c3_b_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_c_transitionTxtStartIdx[2] = { 2U, 11U };

  static const uint32_T c3_c_transitionTxtEndIdx[2] = { 10U, 19U };

  static const int32_T c3_c_postfixPredicateTree[4] = { 0, -1, 1, -2 };

  static const uint32_T c3_d_transitionTxtStartIdx[2] = { 2U, 16U };

  static const uint32_T c3_d_transitionTxtEndIdx[2] = { 10U, 24U };

  static const int32_T c3_d_postfixPredicateTree[4] = { 0, -1, 1, -3 };

  static const uint32_T c3_e_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_e_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_e_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_f_transitionTxtStartIdx[2] = { 0U, 8U };

  static const uint32_T c3_f_transitionTxtEndIdx[2] = { 6U, 15U };

  static const int32_T c3_f_postfixPredicateTree[4] = { 0, 1, -1, -3 };

  static const uint32_T c3_g_transitionTxtStartIdx[1] = { 2U };

  static const uint32_T c3_g_transitionTxtEndIdx[1] = { 16U };

  static const int32_T c3_g_postfixPredicateTree[2] = { 0, -1 };

  static const uint32_T c3_h_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_h_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_h_postfixPredicateTree[1] = { 0 };

  static const int32_T c3_b_relopTxtStartIdx[1] = { 1 };

  static const int32_T c3_b_relopTxtEndIdx[1] = { 9 };

  static const int32_T c3_b_relationalopEps[1] = { 0 };

  static const int32_T c3_b_relationalopType[1] = { 5 };

  static const uint32_T c3_i_transitionTxtStartIdx[1] = { 0U };

  static const uint32_T c3_i_transitionTxtEndIdx[1] = { 11U };

  static const int32_T c3_i_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_j_transitionTxtStartIdx[2] = { 2U, 11U };

  static const uint32_T c3_j_transitionTxtEndIdx[2] = { 10U, 19U };

  static const int32_T c3_j_postfixPredicateTree[4] = { 0, -1, 1, -2 };

  static const uint32_T c3_k_transitionTxtStartIdx[2] = { 2U, 16U };

  static const uint32_T c3_k_transitionTxtEndIdx[2] = { 10U, 24U };

  static const int32_T c3_k_postfixPredicateTree[4] = { 0, -1, 1, -3 };

  static const uint32_T c3_l_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_l_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_l_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_m_transitionTxtStartIdx[1] = { 2U };

  static const uint32_T c3_m_transitionTxtEndIdx[1] = { 16U };

  static const int32_T c3_m_postfixPredicateTree[2] = { 0, -1 };

  static const uint32_T c3_n_transitionTxtStartIdx[2] = { 0U, 8U };

  static const uint32_T c3_n_transitionTxtEndIdx[2] = { 6U, 15U };

  static const int32_T c3_n_postfixPredicateTree[4] = { 0, 1, -1, -3 };

  static const uint32_T c3_o_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_o_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_o_postfixPredicateTree[1] = { 0 };

  static const int32_T c3_c_relopTxtStartIdx[1] = { 1 };

  static const int32_T c3_c_relopTxtEndIdx[1] = { 9 };

  static const int32_T c3_c_relationalopEps[1] = { 0 };

  static const int32_T c3_c_relationalopType[1] = { 5 };

  static const uint32_T c3_p_transitionTxtStartIdx[1] = { 0U };

  static const uint32_T c3_p_transitionTxtEndIdx[1] = { 11U };

  static const int32_T c3_p_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_q_transitionTxtStartIdx[2] = { 2U, 11U };

  static const uint32_T c3_q_transitionTxtEndIdx[2] = { 10U, 19U };

  static const int32_T c3_q_postfixPredicateTree[4] = { 0, -1, 1, -2 };

  static const uint32_T c3_r_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_r_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_r_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_s_transitionTxtStartIdx[2] = { 1U, 15U };

  static const uint32_T c3_s_transitionTxtEndIdx[2] = { 9U, 23U };

  static const int32_T c3_s_postfixPredicateTree[3] = { 0, 1, -3 };

  static const uint32_T c3_t_transitionTxtStartIdx[1] = { 2U };

  static const uint32_T c3_t_transitionTxtEndIdx[1] = { 16U };

  static const int32_T c3_t_postfixPredicateTree[2] = { 0, -1 };

  static const uint32_T c3_u_transitionTxtStartIdx[2] = { 0U, 8U };

  static const uint32_T c3_u_transitionTxtEndIdx[2] = { 6U, 15U };

  static const int32_T c3_u_postfixPredicateTree[4] = { 0, 1, -1, -3 };

  static const uint32_T c3_v_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_v_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_v_postfixPredicateTree[1] = { 0 };

  static const int32_T c3_d_relopTxtStartIdx[1] = { 1 };

  static const int32_T c3_d_relopTxtEndIdx[1] = { 9 };

  static const int32_T c3_d_relationalopEps[1] = { 0 };

  static const int32_T c3_d_relationalopType[1] = { 5 };

  static const uint32_T c3_w_transitionTxtStartIdx[1] = { 0U };

  static const uint32_T c3_w_transitionTxtEndIdx[1] = { 11U };

  static const int32_T c3_w_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_x_transitionTxtStartIdx[2] = { 2U, 11U };

  static const uint32_T c3_x_transitionTxtEndIdx[2] = { 10U, 19U };

  static const int32_T c3_x_postfixPredicateTree[4] = { 0, -1, 1, -2 };

  static const uint32_T c3_y_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_y_transitionTxtEndIdx[1] = { 9U };

  static const int32_T c3_y_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_ab_transitionTxtStartIdx[2] = { 1U, 15U };

  static const uint32_T c3_ab_transitionTxtEndIdx[2] = { 9U, 23U };

  static const int32_T c3_ab_postfixPredicateTree[3] = { 0, 1, -3 };

  static const uint32_T c3_bb_transitionTxtStartIdx[2] = { 0U, 8U };

  static const uint32_T c3_bb_transitionTxtEndIdx[2] = { 6U, 15U };

  static const int32_T c3_bb_postfixPredicateTree[4] = { 0, 1, -1, -3 };

  static const uint32_T c3_cb_transitionTxtStartIdx[1] = { 2U };

  static const uint32_T c3_cb_transitionTxtEndIdx[1] = { 16U };

  static const int32_T c3_cb_postfixPredicateTree[2] = { 0, -1 };

  static const uint32_T c3_db_transitionTxtStartIdx[3] = { 1U, 31U, 61U };

  static const uint32_T c3_db_transitionTxtEndIdx[3] = { 26U, 56U, 86U };

  static const int32_T c3_db_postfixPredicateTree[7] = { 0, 1, -1, -3, 2, -1, -3
  };

  static const uint32_T c3_eb_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_eb_transitionTxtEndIdx[1] = { 26U };

  static const int32_T c3_eb_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_fb_transitionTxtStartIdx[4] = { 2U, 31U, 61U, 91U };

  static const uint32_T c3_fb_transitionTxtEndIdx[4] = { 27U, 56U, 86U, 116U };

  static const int32_T c3_fb_postfixPredicateTree[10] = { 0, -1, 1, -3, 2, -1,
    -3, 3, -1, -3 };

  static const uint32_T c3_gb_transitionTxtStartIdx[2] = { 2U, 31U };

  static const uint32_T c3_gb_transitionTxtEndIdx[2] = { 27U, 56U };

  static const int32_T c3_gb_postfixPredicateTree[4] = { 0, -1, 1, -3 };

  static const uint32_T c3_hb_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_hb_transitionTxtEndIdx[1] = { 26U };

  static const int32_T c3_hb_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_ib_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_ib_transitionTxtEndIdx[1] = { 26U };

  static const int32_T c3_ib_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_jb_transitionTxtStartIdx[3] = { 1U, 31U, 61U };

  static const uint32_T c3_jb_transitionTxtEndIdx[3] = { 26U, 56U, 86U };

  static const int32_T c3_jb_postfixPredicateTree[7] = { 0, 1, -1, -3, 2, -1, -3
  };

  static const uint32_T c3_kb_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_kb_transitionTxtEndIdx[1] = { 26U };

  static const int32_T c3_kb_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_lb_transitionTxtStartIdx[4] = { 2U, 31U, 61U, 91U };

  static const uint32_T c3_lb_transitionTxtEndIdx[4] = { 27U, 56U, 86U, 116U };

  static const int32_T c3_lb_postfixPredicateTree[10] = { 0, -1, 1, -3, 2, -1,
    -3, 3, -1, -3 };

  static const uint32_T c3_mb_transitionTxtStartIdx[2] = { 2U, 31U };

  static const uint32_T c3_mb_transitionTxtEndIdx[2] = { 27U, 56U };

  static const int32_T c3_mb_postfixPredicateTree[4] = { 0, -1, 1, -3 };

  static const uint32_T c3_nb_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_nb_transitionTxtEndIdx[1] = { 26U };

  static const int32_T c3_nb_postfixPredicateTree[1] = { 0 };

  static const uint32_T c3_ob_transitionTxtStartIdx[1] = { 1U };

  static const uint32_T c3_ob_transitionTxtEndIdx[1] = { 26U };

  static const int32_T c3_ob_postfixPredicateTree[1] = { 0 };

  setLegacyDebuggerFlag(chartInstance->S, false);
  setDebuggerFlag(chartInstance->S, true);
  setDataBrowseFcn(chartInstance->S, (void *)c3_chart_data_browse_helper);
  chartInstance->c3_RuntimeVar = sfListenerCacheSimStruct(chartInstance->S);
  sim_mode_is_external(chartInstance->S);
  covrtCreateStateflowInstanceData(chartInstance->c3_covrtInstance, 35U, 3U,
    104U, 42U);
  covrtChartInitFcn(chartInstance->c3_covrtInstance, 1U, false, false, false);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 0U, 4U, false, false, false,
                    0U, &c3_decisionTxtStartIdx, &c3_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 1U, 2U, true, false, false,
                    0U, &c3_b_decisionTxtStartIdx, &c3_b_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 2U, 0U, false, false, false,
                    0U, &c3_c_decisionTxtStartIdx, &c3_c_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 3U, 4U, true, true, false,
                    0U, &c3_d_decisionTxtStartIdx, &c3_d_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 4U, 0U, false, false, false,
                    0U, &c3_e_decisionTxtStartIdx, &c3_e_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 5U, 0U, false, false, false,
                    0U, &c3_f_decisionTxtStartIdx, &c3_f_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 6U, 0U, false, false, false,
                    0U, &c3_g_decisionTxtStartIdx, &c3_g_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 7U, 0U, false, false, false,
                    0U, &c3_h_decisionTxtStartIdx, &c3_h_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 8U, 2U, true, false, false,
                    0U, &c3_i_decisionTxtStartIdx, &c3_i_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 9U, 0U, false, false, false,
                    0U, &c3_j_decisionTxtStartIdx, &c3_j_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 10U, 4U, true, true, false,
                    0U, &c3_k_decisionTxtStartIdx, &c3_k_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 11U, 0U, false, false,
                    false, 0U, &c3_l_decisionTxtStartIdx,
                    &c3_l_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 12U, 0U, false, false,
                    false, 0U, &c3_m_decisionTxtStartIdx,
                    &c3_m_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 13U, 0U, false, false,
                    false, 0U, &c3_n_decisionTxtStartIdx,
                    &c3_n_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 14U, 0U, false, false,
                    false, 0U, &c3_o_decisionTxtStartIdx,
                    &c3_o_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 15U, 2U, true, false, false,
                    0U, &c3_p_decisionTxtStartIdx, &c3_p_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 16U, 0U, false, false,
                    false, 0U, &c3_q_decisionTxtStartIdx,
                    &c3_q_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 17U, 4U, true, true, false,
                    0U, &c3_r_decisionTxtStartIdx, &c3_r_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 18U, 0U, false, false,
                    false, 0U, &c3_s_decisionTxtStartIdx,
                    &c3_s_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 19U, 0U, false, false,
                    false, 0U, &c3_t_decisionTxtStartIdx,
                    &c3_t_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 20U, 0U, false, false,
                    false, 0U, &c3_u_decisionTxtStartIdx,
                    &c3_u_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 21U, 0U, false, false,
                    false, 0U, &c3_v_decisionTxtStartIdx,
                    &c3_v_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 22U, 2U, true, false, false,
                    0U, &c3_w_decisionTxtStartIdx, &c3_w_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 23U, 0U, false, false,
                    false, 0U, &c3_x_decisionTxtStartIdx,
                    &c3_x_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 24U, 4U, true, true, false,
                    0U, &c3_y_decisionTxtStartIdx, &c3_y_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 25U, 0U, false, false,
                    false, 0U, &c3_ab_decisionTxtStartIdx,
                    &c3_ab_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 26U, 0U, false, false,
                    false, 0U, &c3_bb_decisionTxtStartIdx,
                    &c3_bb_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 27U, 0U, false, false,
                    false, 0U, &c3_cb_decisionTxtStartIdx,
                    &c3_cb_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 28U, 0U, false, false,
                    false, 0U, &c3_db_decisionTxtStartIdx,
                    &c3_db_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 29U, 0U, false, false,
                    false, 0U, &c3_eb_decisionTxtStartIdx,
                    &c3_eb_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 30U, 0U, false, false,
                    false, 0U, &c3_fb_decisionTxtStartIdx,
                    &c3_fb_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 31U, 0U, false, false,
                    false, 0U, &c3_gb_decisionTxtStartIdx,
                    &c3_gb_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 32U, 0U, false, false,
                    false, 0U, &c3_hb_decisionTxtStartIdx,
                    &c3_hb_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 33U, 0U, false, false,
                    false, 0U, &c3_ib_decisionTxtStartIdx,
                    &c3_ib_decisionTxtEndIdx);
  covrtStateInitFcn(chartInstance->c3_covrtInstance, 34U, 0U, false, false,
                    false, 0U, &c3_jb_decisionTxtStartIdx,
                    &c3_jb_decisionTxtEndIdx);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 10U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 14U, 1,
                    c3_transitionTxtStartIdx, c3_transitionTxtEndIdx, 1U,
                    c3_postfixPredicateTree);
  covrtRelationalopInitFcn(chartInstance->c3_covrtInstance, 14U, 1,
    c3_relopTxtStartIdx, c3_relopTxtEndIdx, c3_relationalopEps,
    c3_relationalopType);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 9U, 1,
                    c3_b_transitionTxtStartIdx, c3_b_transitionTxtEndIdx, 1U,
                    c3_b_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 15U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 6U, 0, NULL, NULL, 0U, NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 17U, 2,
                    c3_c_transitionTxtStartIdx, c3_c_transitionTxtEndIdx, 4U,
                    c3_c_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 16U, 2,
                    c3_d_transitionTxtStartIdx, c3_d_transitionTxtEndIdx, 4U,
                    c3_d_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 19U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 18U, 1,
                    c3_e_transitionTxtStartIdx, c3_e_transitionTxtEndIdx, 1U,
                    c3_e_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 11U, 2,
                    c3_f_transitionTxtStartIdx, c3_f_transitionTxtEndIdx, 4U,
                    c3_f_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 27U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 12U, 1,
                    c3_g_transitionTxtStartIdx, c3_g_transitionTxtEndIdx, 2U,
                    c3_g_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 47U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 48U, 1,
                    c3_h_transitionTxtStartIdx, c3_h_transitionTxtEndIdx, 1U,
                    c3_h_postfixPredicateTree);
  covrtRelationalopInitFcn(chartInstance->c3_covrtInstance, 48U, 1,
    c3_b_relopTxtStartIdx, c3_b_relopTxtEndIdx, c3_b_relationalopEps,
    c3_b_relationalopType);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 49U, 1,
                    c3_i_transitionTxtStartIdx, c3_i_transitionTxtEndIdx, 1U,
                    c3_i_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 50U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 51U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 0U, 2,
                    c3_j_transitionTxtStartIdx, c3_j_transitionTxtEndIdx, 4U,
                    c3_j_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 2U, 0, NULL, NULL, 0U, NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 22U, 2,
                    c3_k_transitionTxtStartIdx, c3_k_transitionTxtEndIdx, 4U,
                    c3_k_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 23U, 1,
                    c3_l_transitionTxtStartIdx, c3_l_transitionTxtEndIdx, 1U,
                    c3_l_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 7U, 1,
                    c3_m_transitionTxtStartIdx, c3_m_transitionTxtEndIdx, 2U,
                    c3_m_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 21U, 2,
                    c3_n_transitionTxtStartIdx, c3_n_transitionTxtEndIdx, 4U,
                    c3_n_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 20U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 5U, 0, NULL, NULL, 0U, NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 4U, 1,
                    c3_o_transitionTxtStartIdx, c3_o_transitionTxtEndIdx, 1U,
                    c3_o_postfixPredicateTree);
  covrtRelationalopInitFcn(chartInstance->c3_covrtInstance, 4U, 1,
    c3_c_relopTxtStartIdx, c3_c_relopTxtEndIdx, c3_c_relationalopEps,
    c3_c_relationalopType);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 3U, 1,
                    c3_p_transitionTxtStartIdx, c3_p_transitionTxtEndIdx, 1U,
                    c3_p_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 1U, 0, NULL, NULL, 0U, NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 46U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 45U, 2,
                    c3_q_transitionTxtStartIdx, c3_q_transitionTxtEndIdx, 4U,
                    c3_q_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 44U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 43U, 1,
                    c3_r_transitionTxtStartIdx, c3_r_transitionTxtEndIdx, 1U,
                    c3_r_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 42U, 2,
                    c3_s_transitionTxtStartIdx, c3_s_transitionTxtEndIdx, 3U,
                    c3_s_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 39U, 1,
                    c3_t_transitionTxtStartIdx, c3_t_transitionTxtEndIdx, 2U,
                    c3_t_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 41U, 2,
                    c3_u_transitionTxtStartIdx, c3_u_transitionTxtEndIdx, 4U,
                    c3_u_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 40U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 38U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 37U, 1,
                    c3_v_transitionTxtStartIdx, c3_v_transitionTxtEndIdx, 1U,
                    c3_v_postfixPredicateTree);
  covrtRelationalopInitFcn(chartInstance->c3_covrtInstance, 37U, 1,
    c3_d_relopTxtStartIdx, c3_d_relopTxtEndIdx, c3_d_relationalopEps,
    c3_d_relationalopType);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 36U, 1,
                    c3_w_transitionTxtStartIdx, c3_w_transitionTxtEndIdx, 1U,
                    c3_w_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 35U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 34U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 33U, 2,
                    c3_x_transitionTxtStartIdx, c3_x_transitionTxtEndIdx, 4U,
                    c3_x_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 32U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 29U, 1,
                    c3_y_transitionTxtStartIdx, c3_y_transitionTxtEndIdx, 1U,
                    c3_y_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 26U, 2,
                    c3_ab_transitionTxtStartIdx, c3_ab_transitionTxtEndIdx, 3U,
                    c3_ab_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 25U, 2,
                    c3_bb_transitionTxtStartIdx, c3_bb_transitionTxtEndIdx, 4U,
                    c3_bb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 13U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 8U, 1,
                    c3_cb_transitionTxtStartIdx, c3_cb_transitionTxtEndIdx, 2U,
                    c3_cb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 52U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 53U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 54U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 55U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 56U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 57U, 3,
                    c3_db_transitionTxtStartIdx, c3_db_transitionTxtEndIdx, 7U,
                    c3_db_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 58U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 59U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 60U, 1,
                    c3_eb_transitionTxtStartIdx, c3_eb_transitionTxtEndIdx, 1U,
                    c3_eb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 61U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 62U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 63U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 64U, 4,
                    c3_fb_transitionTxtStartIdx, c3_fb_transitionTxtEndIdx, 10U,
                    c3_fb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 65U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 66U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 67U, 2,
                    c3_gb_transitionTxtStartIdx, c3_gb_transitionTxtEndIdx, 4U,
                    c3_gb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 68U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 69U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 70U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 71U, 1,
                    c3_hb_transitionTxtStartIdx, c3_hb_transitionTxtEndIdx, 1U,
                    c3_hb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 72U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 73U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 74U, 1,
                    c3_ib_transitionTxtStartIdx, c3_ib_transitionTxtEndIdx, 1U,
                    c3_ib_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 75U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 76U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 77U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 78U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 79U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 80U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 81U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 82U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 83U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 84U, 3,
                    c3_jb_transitionTxtStartIdx, c3_jb_transitionTxtEndIdx, 7U,
                    c3_jb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 85U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 86U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 87U, 1,
                    c3_kb_transitionTxtStartIdx, c3_kb_transitionTxtEndIdx, 1U,
                    c3_kb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 88U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 89U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 90U, 4,
                    c3_lb_transitionTxtStartIdx, c3_lb_transitionTxtEndIdx, 10U,
                    c3_lb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 91U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 92U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 93U, 2,
                    c3_mb_transitionTxtStartIdx, c3_mb_transitionTxtEndIdx, 4U,
                    c3_mb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 94U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 95U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 96U, 1,
                    c3_nb_transitionTxtStartIdx, c3_nb_transitionTxtEndIdx, 1U,
                    c3_nb_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 97U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 98U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 99U, 1,
                    c3_ob_transitionTxtStartIdx, c3_ob_transitionTxtEndIdx, 1U,
                    c3_ob_postfixPredicateTree);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 100U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 101U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 102U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 103U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 28U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 30U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 31U, 0, NULL, NULL, 0U,
                    NULL);
  covrtTransInitFcn(chartInstance->c3_covrtInstance, 24U, 0, NULL, NULL, 0U,
                    NULL);
}

static void initSimStructsc3_sf_aircraft_fault
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void c3_LO(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  switch (chartInstance->c3_is_LO) {
   case c3_IN_Isolated:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 8, 0, c3_IN_Isolated);
    break;

   case c3_IN_L1:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 8, 0, c3_IN_L1);
    c3_L1(chartInstance);
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 8, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_LO = c3_IN_NO_ACTIVE_CHILD;
    break;
  }
}

static void c3_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  boolean_T c3_d_out;
  real_T c3_d;
  real_T c3_d1;
  real_T c3_d2;
  int32_T c3_b_previousEvent;
  boolean_T c3_e_out;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  boolean_T c3_f_out;
  boolean_T c3_g_out;
  real_T c3_d3;
  real_T c3_d4;
  real_T c3_d5;
  boolean_T c3_d_temp;
  boolean_T c3_h_out;
  real_T c3_d6;
  c3_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U, 9U,
    0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 9U, 0,
    (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U) != 0U);
  if (c3_out) {
    chartInstance->c3_JITTransitionAnimation[9U] = 1U;
    c3_exit_internal_L1(chartInstance);
    chartInstance->c3_is_LO = c3_IN_NO_ACTIVE_CHILD;
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    if (chartInstance->c3_is_active_LI != 0U) {
      c3_LI(chartInstance);
    }

    chartInstance->c3_sfEvent = c3_previousEvent;
    if ((chartInstance->c3_is_LO == c3_IN_NO_ACTIVE_CHILD) &&
        (!(chartInstance->c3_is_active_LO == 0U))) {
      chartInstance->c3_is_LO = c3_IN_Isolated;
    }
  } else {
    c3_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 11U, 0,
      (chartInstance->c3_sfEvent == c3_event_go_off) != 0U);
    if (c3_temp) {
      c3_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 11U, 1,
        (*chartInstance->c3_LO_mode == Off) != 0U);
    }

    c3_b_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
      11U, 0U, c3_temp != 0U);
    if (c3_b_out) {
      chartInstance->c3_JITTransitionAnimation[11U] = 1U;
      c3_c_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
        14U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 14U, 0,
        (boolean_T)covrtRelationalopUpdateFcn(chartInstance->c3_covrtInstance,
        5U, 14U, 0U, (real_T)chartInstance->c3_fails, 5.0, 0, 5U,
        chartInstance->c3_fails >= 5) != 0U) != 0U);
      if (c3_c_out) {
        chartInstance->c3_JITTransitionAnimation[14U] = 1U;
        c3_exit_internal_L1(chartInstance);
        chartInstance->c3_is_LO = c3_IN_NO_ACTIVE_CHILD;
        chartInstance->c3_is_LO = c3_IN_Isolated;
      } else {
        chartInstance->c3_JITTransitionAnimation[27U] = 1U;
        c3_exit_internal_L1(chartInstance);
        c3_b_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        if (chartInstance->c3_is_active_LI != 0U) {
          c3_LI(chartInstance);
        }

        chartInstance->c3_sfEvent = c3_b_previousEvent;
        if ((*chartInstance->c3_LO_mode == Isolated) &&
            (!(chartInstance->c3_is_LO != c3_IN_L1))) {
          *chartInstance->c3_LO_mode = Off;
        }
      }
    } else {
      switch (*chartInstance->c3_LO_mode) {
       case Passive:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 0, 3);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, 0.0);
        chartInstance->c3_JITTransitionAnimation[30U] = 1U;
        c3_d = (real_T)(*chartInstance->c3_LI_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, c3_d);
        c3_e_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 18U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          18U, 0, (c3_d != 0.0) != 0U) != 0U);
        if (c3_e_out) {
          chartInstance->c3_JITTransitionAnimation[18U] = 1U;
          *chartInstance->c3_LO_mode = Isolated;
          *chartInstance->c3_LO_mode = Standby;
        } else {
          chartInstance->c3_JITTransitionAnimation[6U] = 1U;
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, 0.0);
          chartInstance->c3_JITTransitionAnimation[30U] = 1U;
          c3_d4 = (real_T)(*chartInstance->c3_LI_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, c3_d4);
          c3_d_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            17U, 0, (c3_d4 != 0.0) != 0U);
          if (!c3_d_temp) {
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
            chartInstance->c3_JITTransitionAnimation[31U] = 1U;
            c3_d6 = (real_T)(*chartInstance->c3_RO_mode == Active);
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d6);
            c3_d_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
              17U, 1, (c3_d6 != 0.0) != 0U);
          }

          c3_h_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
            5U, 17U, 0U, c3_d_temp != 0U);
          if (c3_h_out) {
            chartInstance->c3_JITTransitionAnimation[17U] = 1U;
            *chartInstance->c3_LO_mode = Isolated;
            *chartInstance->c3_LO_mode = Active;
          }
        }
        break;

       case Standby:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 0, 4);
        chartInstance->c3_JITTransitionAnimation[19U] = 1U;
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, 0.0);
        chartInstance->c3_JITTransitionAnimation[30U] = 1U;
        c3_d2 = (real_T)(*chartInstance->c3_LI_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, c3_d2);
        c3_c_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 17U,
          0, (c3_d2 != 0.0) != 0U);
        if (!c3_c_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
          chartInstance->c3_JITTransitionAnimation[31U] = 1U;
          c3_d5 = (real_T)(*chartInstance->c3_RO_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d5);
          c3_c_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            17U, 1, (c3_d5 != 0.0) != 0U);
        }

        c3_g_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 17U, 0U, c3_c_temp != 0U);
        if (c3_g_out) {
          chartInstance->c3_JITTransitionAnimation[17U] = 1U;
          *chartInstance->c3_LO_mode = Isolated;
          *chartInstance->c3_LO_mode = Active;
        }
        break;

       case Active:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 0, 1);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
        chartInstance->c3_JITTransitionAnimation[31U] = 1U;
        c3_d1 = (real_T)(*chartInstance->c3_RO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d1);
        c3_b_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 16U,
          0, (c3_d1 != 0.0) != 0U);
        if (c3_b_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, 0.0);
          chartInstance->c3_JITTransitionAnimation[30U] = 1U;
          c3_d3 = (real_T)(*chartInstance->c3_LI_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, c3_d3);
          c3_b_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            16U, 1, (c3_d3 != 0.0) != 0U);
        }

        c3_f_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 16U, 0U, c3_b_temp != 0U);
        if (c3_f_out) {
          chartInstance->c3_JITTransitionAnimation[16U] = 1U;
          *chartInstance->c3_LO_mode = Isolated;
          *chartInstance->c3_LO_mode = Standby;
        }
        break;

       case Off:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 0, 2);
        c3_d_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 12U, 0U, (!covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          12U, 0, ((boolean_T *)&((char_T *)chartInstance->c3_u)[72])[0] != 0U))
          != 0U);
        if (c3_d_out) {
          chartInstance->c3_JITTransitionAnimation[12U] = 1U;
          chartInstance->c3_fails = c3__s32_add__(chartInstance,
            chartInstance->c3_fails, 1, 0, 36U, 7, 7);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 0U, (real_T)
                            chartInstance->c3_fails);
          *chartInstance->c3_LO_mode = Isolated;
          chartInstance->c3_JITTransitionAnimation[15U] = 1U;
          *chartInstance->c3_LO_mode = Passive;
        }
        break;

       default:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_LO_mode = Isolated;
        break;
      }
    }
  }
}

static void c3_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  switch (*chartInstance->c3_LO_mode) {
   case Active:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 1, 1);
    *chartInstance->c3_LO_mode = Isolated;
    break;

   case Off:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 1, 2);
    chartInstance->c3_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_fails, 1, 0, 36U, 7, 7);
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 0U, (real_T)
                      chartInstance->c3_fails);
    *chartInstance->c3_LO_mode = Isolated;
    break;

   case Passive:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 1, 3);
    *chartInstance->c3_LO_mode = Isolated;
    break;

   case Standby:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 1, 4);
    *chartInstance->c3_LO_mode = Isolated;
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 10, 1, 0);
    *chartInstance->c3_LO_mode = Isolated;
    break;
  }
}

static void c3_RO(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  switch (chartInstance->c3_is_RO) {
   case c3_IN_Isolated:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 22, 0, c3_IN_Isolated);
    break;

   case c3_IN_L1:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 22, 0, c3_IN_L1);
    c3_b_L1(chartInstance);
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 22, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_RO = c3_IN_NO_ACTIVE_CHILD;
    break;
  }
}

static void c3_b_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  boolean_T c3_d_out;
  real_T c3_d;
  real_T c3_d1;
  real_T c3_d2;
  int32_T c3_b_previousEvent;
  boolean_T c3_e_out;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  boolean_T c3_f_out;
  boolean_T c3_g_out;
  real_T c3_d3;
  real_T c3_d4;
  real_T c3_d5;
  boolean_T c3_d_temp;
  boolean_T c3_h_out;
  real_T c3_d6;
  c3_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U, 49U,
    0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 49U, 0,
    (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U) != 0U);
  if (c3_out) {
    chartInstance->c3_JITTransitionAnimation[49U] = 1U;
    c3_b_exit_internal_L1(chartInstance);
    chartInstance->c3_is_RO = c3_IN_NO_ACTIVE_CHILD;
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    if (chartInstance->c3_is_active_RI != 0U) {
      c3_RI(chartInstance);
    }

    chartInstance->c3_sfEvent = c3_previousEvent;
    if ((chartInstance->c3_is_RO == c3_IN_NO_ACTIVE_CHILD) &&
        (!(chartInstance->c3_is_active_RO == 0U))) {
      chartInstance->c3_is_RO = c3_IN_Isolated;
    }
  } else {
    c3_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 21U, 0,
      (chartInstance->c3_sfEvent == c3_event_go_off) != 0U);
    if (c3_temp) {
      c3_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 21U, 1,
        (*chartInstance->c3_RO_mode == Off) != 0U);
    }

    c3_b_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
      21U, 0U, c3_temp != 0U);
    if (c3_b_out) {
      chartInstance->c3_JITTransitionAnimation[21U] = 1U;
      c3_c_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
        48U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 48U, 0,
        (boolean_T)covrtRelationalopUpdateFcn(chartInstance->c3_covrtInstance,
        5U, 48U, 0U, (real_T)chartInstance->c3_b_fails, 5.0, 0, 5U,
        chartInstance->c3_b_fails >= 5) != 0U) != 0U);
      if (c3_c_out) {
        chartInstance->c3_JITTransitionAnimation[48U] = 1U;
        c3_b_exit_internal_L1(chartInstance);
        chartInstance->c3_is_RO = c3_IN_NO_ACTIVE_CHILD;
        chartInstance->c3_is_RO = c3_IN_Isolated;
      } else {
        chartInstance->c3_JITTransitionAnimation[20U] = 1U;
        c3_b_exit_internal_L1(chartInstance);
        c3_b_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        if (chartInstance->c3_is_active_RI != 0U) {
          c3_RI(chartInstance);
        }

        chartInstance->c3_sfEvent = c3_b_previousEvent;
        if ((*chartInstance->c3_RO_mode == Isolated) &&
            (!(chartInstance->c3_is_RO != c3_IN_L1))) {
          *chartInstance->c3_RO_mode = Off;
        }
      }
    } else {
      switch (*chartInstance->c3_RO_mode) {
       case Passive:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 0, 3);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, 0.0);
        chartInstance->c3_JITTransitionAnimation[24U] = 1U;
        c3_d = (real_T)(*chartInstance->c3_RI_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, c3_d);
        c3_e_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 23U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          23U, 0, (c3_d != 0.0) != 0U) != 0U);
        if (c3_e_out) {
          chartInstance->c3_JITTransitionAnimation[23U] = 1U;
          *chartInstance->c3_RO_mode = Isolated;
          *chartInstance->c3_RO_mode = Standby;
        } else {
          chartInstance->c3_JITTransitionAnimation[51U] = 1U;
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, 0.0);
          chartInstance->c3_JITTransitionAnimation[24U] = 1U;
          c3_d4 = (real_T)(*chartInstance->c3_RI_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, c3_d4);
          c3_d_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            0U, 0, (c3_d4 != 0.0) != 0U);
          if (!c3_d_temp) {
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
            chartInstance->c3_JITTransitionAnimation[28U] = 1U;
            c3_d6 = (real_T)(*chartInstance->c3_LO_mode == Active);
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d6);
            c3_d_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
              0U, 1, (c3_d6 != 0.0) != 0U);
          }

          c3_h_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
            5U, 0U, 0U, c3_d_temp != 0U);
          if (c3_h_out) {
            chartInstance->c3_JITTransitionAnimation[0U] = 1U;
            *chartInstance->c3_RO_mode = Isolated;
            *chartInstance->c3_RO_mode = Active;
          }
        }
        break;

       case Standby:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 0, 4);
        chartInstance->c3_JITTransitionAnimation[2U] = 1U;
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, 0.0);
        chartInstance->c3_JITTransitionAnimation[24U] = 1U;
        c3_d2 = (real_T)(*chartInstance->c3_RI_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, c3_d2);
        c3_c_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 0U,
          0, (c3_d2 != 0.0) != 0U);
        if (!c3_c_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
          chartInstance->c3_JITTransitionAnimation[28U] = 1U;
          c3_d5 = (real_T)(*chartInstance->c3_LO_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d5);
          c3_c_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 0U,
            1, (c3_d5 != 0.0) != 0U);
        }

        c3_g_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 0U, 0U, c3_c_temp != 0U);
        if (c3_g_out) {
          chartInstance->c3_JITTransitionAnimation[0U] = 1U;
          *chartInstance->c3_RO_mode = Isolated;
          *chartInstance->c3_RO_mode = Active;
        }
        break;

       case Active:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 0, 1);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
        chartInstance->c3_JITTransitionAnimation[28U] = 1U;
        c3_d1 = (real_T)(*chartInstance->c3_LO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d1);
        c3_b_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 22U,
          0, (c3_d1 != 0.0) != 0U);
        if (c3_b_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, 0.0);
          chartInstance->c3_JITTransitionAnimation[24U] = 1U;
          c3_d3 = (real_T)(*chartInstance->c3_RI_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, c3_d3);
          c3_b_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            22U, 1, (c3_d3 != 0.0) != 0U);
        }

        c3_f_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 22U, 0U, c3_b_temp != 0U);
        if (c3_f_out) {
          chartInstance->c3_JITTransitionAnimation[22U] = 1U;
          *chartInstance->c3_RO_mode = Isolated;
          *chartInstance->c3_RO_mode = Standby;
        }
        break;

       case Off:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 0, 2);
        c3_d_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 7U, 0U, (!covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          7U, 0, ((boolean_T *)&((char_T *)chartInstance->c3_u)[72])[2] != 0U))
          != 0U);
        if (c3_d_out) {
          chartInstance->c3_JITTransitionAnimation[7U] = 1U;
          chartInstance->c3_b_fails = c3__s32_add__(chartInstance,
            chartInstance->c3_b_fails, 1, 0, 20U, 7, 7);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 1U, (real_T)
                            chartInstance->c3_b_fails);
          *chartInstance->c3_RO_mode = Isolated;
          chartInstance->c3_JITTransitionAnimation[50U] = 1U;
          *chartInstance->c3_RO_mode = Passive;
        }
        break;

       default:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_RO_mode = Isolated;
        break;
      }
    }
  }
}

static void c3_b_exit_internal_L1(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  switch (*chartInstance->c3_RO_mode) {
   case Active:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 1, 1);
    *chartInstance->c3_RO_mode = Isolated;
    break;

   case Off:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 1, 2);
    chartInstance->c3_b_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_b_fails, 1, 0, 20U, 7, 7);
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 1U, (real_T)
                      chartInstance->c3_b_fails);
    *chartInstance->c3_RO_mode = Isolated;
    break;

   case Passive:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 1, 3);
    *chartInstance->c3_RO_mode = Isolated;
    break;

   case Standby:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 1, 4);
    *chartInstance->c3_RO_mode = Isolated;
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 24, 1, 0);
    *chartInstance->c3_RO_mode = Isolated;
    break;
  }
}

static void c3_LI(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  switch (chartInstance->c3_is_LI) {
   case c3_IN_Isolated:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 1, 0, c3_IN_Isolated);
    break;

   case c3_IN_L1:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 1, 0, c3_IN_L1);
    c3_c_L1(chartInstance);
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 1, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_LI = c3_IN_NO_ACTIVE_CHILD;
    break;
  }
}

static void c3_c_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  boolean_T c3_d_out;
  real_T c3_d;
  real_T c3_d1;
  int32_T c3_b_previousEvent;
  real_T c3_d2;
  int32_T c3_c_previousEvent;
  boolean_T c3_e_out;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  boolean_T c3_f_out;
  boolean_T c3_g_out;
  real_T c3_d3;
  real_T c3_d4;
  real_T c3_d5;
  int32_T c3_d_previousEvent;
  boolean_T c3_d_temp;
  boolean_T c3_h_out;
  real_T c3_d6;
  c3_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U, 3U,
    0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 3U, 0,
    (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U) != 0U);
  if (c3_out) {
    chartInstance->c3_JITTransitionAnimation[3U] = 1U;
    c3_c_exit_internal_L1(chartInstance);
    chartInstance->c3_is_LI = c3_IN_NO_ACTIVE_CHILD;
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    if (chartInstance->c3_is_active_LO != 0U) {
      c3_LO(chartInstance);
    }

    chartInstance->c3_sfEvent = c3_previousEvent;
    if ((chartInstance->c3_is_LI == c3_IN_NO_ACTIVE_CHILD) &&
        (chartInstance->c3_is_active_LI != 0U)) {
      c3_b_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_E;
      if (chartInstance->c3_is_active_RO != 0U) {
        c3_RO(chartInstance);
      }

      chartInstance->c3_sfEvent = c3_b_previousEvent;
    }

    if ((chartInstance->c3_is_LI == c3_IN_NO_ACTIVE_CHILD) &&
        (chartInstance->c3_is_active_LI != 0U) && (chartInstance->c3_is_LI ==
         c3_IN_NO_ACTIVE_CHILD) && (chartInstance->c3_is_active_LI != 0U)) {
      chartInstance->c3_is_LI = c3_IN_Isolated;
    }
  } else {
    c3_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 41U, 0,
      (chartInstance->c3_sfEvent == c3_event_go_off) != 0U);
    if (c3_temp) {
      c3_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 41U, 1,
        (*chartInstance->c3_LI_mode == Off) != 0U);
    }

    c3_b_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
      41U, 0U, c3_temp != 0U);
    if (c3_b_out) {
      chartInstance->c3_JITTransitionAnimation[41U] = 1U;
      c3_c_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
        4U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 4U, 0,
        (boolean_T)covrtRelationalopUpdateFcn(chartInstance->c3_covrtInstance,
        5U, 4U, 0U, (real_T)chartInstance->c3_c_fails, 5.0, 0, 5U,
        chartInstance->c3_c_fails >= 5) != 0U) != 0U);
      if (c3_c_out) {
        chartInstance->c3_JITTransitionAnimation[4U] = 1U;
        c3_c_exit_internal_L1(chartInstance);
        chartInstance->c3_is_LI = c3_IN_NO_ACTIVE_CHILD;
        chartInstance->c3_is_LI = c3_IN_Isolated;
      } else {
        chartInstance->c3_JITTransitionAnimation[40U] = 1U;
        c3_c_exit_internal_L1(chartInstance);
        c3_c_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        if (chartInstance->c3_is_active_LO != 0U) {
          c3_LO(chartInstance);
        }

        chartInstance->c3_sfEvent = c3_c_previousEvent;
        if ((*chartInstance->c3_LI_mode == Isolated) && (chartInstance->c3_is_LI
             == c3_IN_L1)) {
          c3_d_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_E;
          if (chartInstance->c3_is_active_RO != 0U) {
            c3_RO(chartInstance);
          }

          chartInstance->c3_sfEvent = c3_d_previousEvent;
        }

        if ((*chartInstance->c3_LI_mode == Isolated) && (chartInstance->c3_is_LI
             == c3_IN_L1) && (*chartInstance->c3_LI_mode == Isolated) &&
            (chartInstance->c3_is_LI == c3_IN_L1)) {
          *chartInstance->c3_LI_mode = Off;
        }
      }
    } else {
      switch (*chartInstance->c3_LI_mode) {
       case Passive:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 0, 3);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
        chartInstance->c3_JITTransitionAnimation[28U] = 1U;
        c3_d = (real_T)(*chartInstance->c3_LO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d);
        c3_e_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 43U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          43U, 0, (c3_d != 0.0) != 0U) != 0U);
        if (c3_e_out) {
          chartInstance->c3_JITTransitionAnimation[43U] = 1U;
          *chartInstance->c3_LI_mode = Isolated;
          *chartInstance->c3_LI_mode = Standby;
        } else {
          chartInstance->c3_JITTransitionAnimation[46U] = 1U;
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
          chartInstance->c3_JITTransitionAnimation[28U] = 1U;
          c3_d4 = (real_T)(*chartInstance->c3_LO_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d4);
          c3_d_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            45U, 0, (c3_d4 != 0.0) != 0U);
          if (!c3_d_temp) {
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, 0.0);
            chartInstance->c3_JITTransitionAnimation[24U] = 1U;
            c3_d6 = (real_T)(*chartInstance->c3_RI_mode == Active);
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, c3_d6);
            c3_d_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
              45U, 1, (c3_d6 != 0.0) != 0U);
          }

          c3_h_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
            5U, 45U, 0U, c3_d_temp != 0U);
          if (c3_h_out) {
            chartInstance->c3_JITTransitionAnimation[45U] = 1U;
            *chartInstance->c3_LI_mode = Isolated;
            *chartInstance->c3_LI_mode = Active;
            c3_enter_atomic_Active(chartInstance);
          }
        }
        break;

       case Standby:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 0, 4);
        chartInstance->c3_JITTransitionAnimation[44U] = 1U;
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
        chartInstance->c3_JITTransitionAnimation[28U] = 1U;
        c3_d2 = (real_T)(*chartInstance->c3_LO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d2);
        c3_c_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 45U,
          0, (c3_d2 != 0.0) != 0U);
        if (!c3_c_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, 0.0);
          chartInstance->c3_JITTransitionAnimation[24U] = 1U;
          c3_d5 = (real_T)(*chartInstance->c3_RI_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 17U, c3_d5);
          c3_c_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            45U, 1, (c3_d5 != 0.0) != 0U);
        }

        c3_g_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 45U, 0U, c3_c_temp != 0U);
        if (c3_g_out) {
          chartInstance->c3_JITTransitionAnimation[45U] = 1U;
          *chartInstance->c3_LI_mode = Isolated;
          *chartInstance->c3_LI_mode = Active;
          c3_enter_atomic_Active(chartInstance);
        }
        break;

       case Active:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 0, 1);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
        chartInstance->c3_JITTransitionAnimation[31U] = 1U;
        c3_d1 = (real_T)(*chartInstance->c3_RO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d1);
        c3_b_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 42U,
          0, (c3_d1 != 0.0) != 0U);
        if (c3_b_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
          chartInstance->c3_JITTransitionAnimation[28U] = 1U;
          c3_d3 = (real_T)(*chartInstance->c3_LO_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d3);
          c3_b_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            42U, 1, (c3_d3 != 0.0) != 0U);
        }

        c3_f_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 42U, 0U, c3_b_temp != 0U);
        if (c3_f_out) {
          chartInstance->c3_JITTransitionAnimation[42U] = 1U;
          *chartInstance->c3_LI_mode = Isolated;
          *chartInstance->c3_LI_mode = Standby;
        }
        break;

       case Off:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 0, 2);
        c3_d_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 39U, 0U, (!covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          39U, 0, ((boolean_T *)&((char_T *)chartInstance->c3_u)[72])[1] != 0U))
          != 0U);
        if (c3_d_out) {
          chartInstance->c3_JITTransitionAnimation[39U] = 1U;
          chartInstance->c3_c_fails = c3__s32_add__(chartInstance,
            chartInstance->c3_c_fails, 1, 0, 27U, 7, 7);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 2U, (real_T)
                            chartInstance->c3_c_fails);
          *chartInstance->c3_LI_mode = Isolated;
          chartInstance->c3_JITTransitionAnimation[1U] = 1U;
          *chartInstance->c3_LI_mode = Passive;
        }
        break;

       default:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_LI_mode = Isolated;
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
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 1, 1);
    *chartInstance->c3_LI_mode = Isolated;
    break;

   case Off:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 1, 2);
    chartInstance->c3_c_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_c_fails, 1, 0, 27U, 7, 7);
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 2U, (real_T)
                      chartInstance->c3_c_fails);
    *chartInstance->c3_LI_mode = Isolated;
    break;

   case Passive:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 1, 3);
    *chartInstance->c3_LI_mode = Isolated;
    break;

   case Standby:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 1, 4);
    *chartInstance->c3_LI_mode = Isolated;
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 3, 1, 0);
    *chartInstance->c3_LI_mode = Isolated;
    break;
  }
}

static void c3_enter_atomic_Active(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  int32_T c3_previousEvent;
  c3_previousEvent = chartInstance->c3_sfEvent;
  chartInstance->c3_sfEvent = c3_event_E;
  if (chartInstance->c3_is_active_LO != 0U) {
    c3_LO(chartInstance);
  }

  chartInstance->c3_sfEvent = c3_previousEvent;
}

static void c3_RI(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  _SF_MEX_LISTEN_FOR_CTRL_C(chartInstance->S);
  switch (chartInstance->c3_is_RI) {
   case c3_IN_Isolated:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 15, 0, c3_IN_Isolated);
    break;

   case c3_IN_L1:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 15, 0, c3_IN_L1);
    c3_d_L1(chartInstance);
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 15, 0, 0);

    /* Unreachable state, for coverage only */
    chartInstance->c3_is_RI = c3_IN_NO_ACTIVE_CHILD;
    break;
  }
}

static void c3_d_L1(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_out;
  boolean_T c3_temp;
  boolean_T c3_b_out;
  int32_T c3_previousEvent;
  boolean_T c3_c_out;
  boolean_T c3_d_out;
  real_T c3_d;
  real_T c3_d1;
  int32_T c3_b_previousEvent;
  real_T c3_d2;
  int32_T c3_c_previousEvent;
  boolean_T c3_e_out;
  boolean_T c3_b_temp;
  boolean_T c3_c_temp;
  boolean_T c3_f_out;
  boolean_T c3_g_out;
  real_T c3_d3;
  int32_T c3_d_previousEvent;
  real_T c3_d4;
  real_T c3_d5;
  int32_T c3_e_previousEvent;
  boolean_T c3_d_temp;
  boolean_T c3_h_out;
  real_T c3_d6;
  int32_T c3_f_previousEvent;
  c3_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U, 36U,
    0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 36U, 0,
    (chartInstance->c3_sfEvent == c3_event_go_isolated) != 0U) != 0U);
  if (c3_out) {
    chartInstance->c3_JITTransitionAnimation[36U] = 1U;
    c3_d_exit_internal_L1(chartInstance);
    chartInstance->c3_is_RI = c3_IN_NO_ACTIVE_CHILD;
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_E;
    if (chartInstance->c3_is_active_RO != 0U) {
      c3_RO(chartInstance);
    }

    chartInstance->c3_sfEvent = c3_previousEvent;
    if ((chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) &&
        (chartInstance->c3_is_active_RI != 0U)) {
      c3_b_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_E;
      if (chartInstance->c3_is_active_LO != 0U) {
        c3_LO(chartInstance);
      }

      chartInstance->c3_sfEvent = c3_b_previousEvent;
      if ((chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) &&
          (chartInstance->c3_is_active_RI != 0U)) {
        c3_d_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        if (chartInstance->c3_is_active_LI != 0U) {
          c3_LI(chartInstance);
        }

        chartInstance->c3_sfEvent = c3_d_previousEvent;
      }
    }

    if ((chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) &&
        (chartInstance->c3_is_active_RI != 0U) && (chartInstance->c3_is_RI ==
         c3_IN_NO_ACTIVE_CHILD) && (chartInstance->c3_is_active_RI != 0U) &&
        (chartInstance->c3_is_RI == c3_IN_NO_ACTIVE_CHILD) &&
        (chartInstance->c3_is_active_RI != 0U)) {
      chartInstance->c3_is_RI = c3_IN_Isolated;
    }
  } else {
    c3_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 25U, 0,
      (chartInstance->c3_sfEvent == c3_event_go_off) != 0U);
    if (c3_temp) {
      c3_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 25U, 1,
        (*chartInstance->c3_RI_mode == Off) != 0U);
    }

    c3_b_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
      25U, 0U, c3_temp != 0U);
    if (c3_b_out) {
      chartInstance->c3_JITTransitionAnimation[25U] = 1U;
      c3_c_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
        37U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 37U, 0,
        (boolean_T)covrtRelationalopUpdateFcn(chartInstance->c3_covrtInstance,
        5U, 37U, 0U, (real_T)chartInstance->c3_d_fails, 5.0, 0, 5U,
        chartInstance->c3_d_fails >= 5) != 0U) != 0U);
      if (c3_c_out) {
        chartInstance->c3_JITTransitionAnimation[37U] = 1U;
        c3_d_exit_internal_L1(chartInstance);
        chartInstance->c3_is_RI = c3_IN_NO_ACTIVE_CHILD;
        chartInstance->c3_is_RI = c3_IN_Isolated;
      } else {
        chartInstance->c3_JITTransitionAnimation[13U] = 1U;
        c3_d_exit_internal_L1(chartInstance);
        c3_c_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_E;
        if (chartInstance->c3_is_active_RO != 0U) {
          c3_RO(chartInstance);
        }

        chartInstance->c3_sfEvent = c3_c_previousEvent;
        if ((*chartInstance->c3_RI_mode == Isolated) && (chartInstance->c3_is_RI
             == c3_IN_L1)) {
          c3_e_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_E;
          if (chartInstance->c3_is_active_LO != 0U) {
            c3_LO(chartInstance);
          }

          chartInstance->c3_sfEvent = c3_e_previousEvent;
          if ((*chartInstance->c3_RI_mode == Isolated) &&
              (chartInstance->c3_is_RI == c3_IN_L1)) {
            c3_f_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_E;
            if (chartInstance->c3_is_active_LI != 0U) {
              c3_LI(chartInstance);
            }

            chartInstance->c3_sfEvent = c3_f_previousEvent;
          }
        }

        if ((*chartInstance->c3_RI_mode == Isolated) && (chartInstance->c3_is_RI
             == c3_IN_L1) && (*chartInstance->c3_RI_mode == Isolated) &&
            (chartInstance->c3_is_RI == c3_IN_L1) && (*chartInstance->c3_RI_mode
             == Isolated) && (chartInstance->c3_is_RI == c3_IN_L1)) {
          *chartInstance->c3_RI_mode = Off;
        }
      }
    } else {
      switch (*chartInstance->c3_RI_mode) {
       case Passive:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 0, 3);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
        chartInstance->c3_JITTransitionAnimation[31U] = 1U;
        c3_d = (real_T)(*chartInstance->c3_RO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d);
        c3_e_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 29U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          29U, 0, (c3_d != 0.0) != 0U) != 0U);
        if (c3_e_out) {
          chartInstance->c3_JITTransitionAnimation[29U] = 1U;
          *chartInstance->c3_RI_mode = Isolated;
          *chartInstance->c3_RI_mode = Standby;
        } else {
          chartInstance->c3_JITTransitionAnimation[34U] = 1U;
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
          chartInstance->c3_JITTransitionAnimation[31U] = 1U;
          c3_d4 = (real_T)(*chartInstance->c3_RO_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d4);
          c3_d_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            33U, 0, (c3_d4 != 0.0) != 0U);
          if (!c3_d_temp) {
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, 0.0);
            chartInstance->c3_JITTransitionAnimation[30U] = 1U;
            c3_d6 = (real_T)(*chartInstance->c3_LI_mode == Active);
            covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, c3_d6);
            c3_d_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
              33U, 1, (c3_d6 != 0.0) != 0U);
          }

          c3_h_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
            5U, 33U, 0U, c3_d_temp != 0U);
          if (c3_h_out) {
            chartInstance->c3_JITTransitionAnimation[33U] = 1U;
            *chartInstance->c3_RI_mode = Isolated;
            *chartInstance->c3_RI_mode = Active;
            c3_b_enter_atomic_Active(chartInstance);
          }
        }
        break;

       case Standby:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 0, 4);
        chartInstance->c3_JITTransitionAnimation[32U] = 1U;
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
        chartInstance->c3_JITTransitionAnimation[31U] = 1U;
        c3_d2 = (real_T)(*chartInstance->c3_RO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d2);
        c3_c_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 33U,
          0, (c3_d2 != 0.0) != 0U);
        if (!c3_c_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, 0.0);
          chartInstance->c3_JITTransitionAnimation[30U] = 1U;
          c3_d5 = (real_T)(*chartInstance->c3_LI_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 19U, c3_d5);
          c3_c_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            33U, 1, (c3_d5 != 0.0) != 0U);
        }

        c3_g_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 33U, 0U, c3_c_temp != 0U);
        if (c3_g_out) {
          chartInstance->c3_JITTransitionAnimation[33U] = 1U;
          *chartInstance->c3_RI_mode = Isolated;
          *chartInstance->c3_RI_mode = Active;
          c3_b_enter_atomic_Active(chartInstance);
        }
        break;

       case Active:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 0, 1);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, 0.0);
        chartInstance->c3_JITTransitionAnimation[28U] = 1U;
        c3_d1 = (real_T)(*chartInstance->c3_LO_mode == Active);
        covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 20U, c3_d1);
        c3_b_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 26U,
          0, (c3_d1 != 0.0) != 0U);
        if (c3_b_temp) {
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, 0.0);
          chartInstance->c3_JITTransitionAnimation[31U] = 1U;
          c3_d3 = (real_T)(*chartInstance->c3_RO_mode == Active);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 18U, c3_d3);
          c3_b_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            26U, 1, (c3_d3 != 0.0) != 0U);
        }

        c3_f_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 26U, 0U, c3_b_temp != 0U);
        if (c3_f_out) {
          chartInstance->c3_JITTransitionAnimation[26U] = 1U;
          *chartInstance->c3_RI_mode = Isolated;
          *chartInstance->c3_RI_mode = Standby;
        }
        break;

       case Off:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 0, 2);
        c3_d_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 8U, 0U, (!covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
          8U, 0, ((boolean_T *)&((char_T *)chartInstance->c3_u)[72])[1] != 0U))
          != 0U);
        if (c3_d_out) {
          chartInstance->c3_JITTransitionAnimation[8U] = 1U;
          chartInstance->c3_d_fails = c3__s32_add__(chartInstance,
            chartInstance->c3_d_fails, 1, 0, 34U, 7, 7);
          covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 3U, (real_T)
                            chartInstance->c3_d_fails);
          *chartInstance->c3_RI_mode = Isolated;
          chartInstance->c3_JITTransitionAnimation[35U] = 1U;
          *chartInstance->c3_RI_mode = Passive;
        }
        break;

       default:
        covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 0, 0);

        /* Unreachable state, for coverage only */
        *chartInstance->c3_RI_mode = Isolated;
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
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 1, 1);
    *chartInstance->c3_RI_mode = Isolated;
    break;

   case Off:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 1, 2);
    chartInstance->c3_d_fails = c3__s32_add__(chartInstance,
      chartInstance->c3_d_fails, 1, 0, 34U, 7, 7);
    covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 3U, (real_T)
                      chartInstance->c3_d_fails);
    *chartInstance->c3_RI_mode = Isolated;
    break;

   case Passive:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 1, 3);
    *chartInstance->c3_RI_mode = Isolated;
    break;

   case Standby:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 1, 4);
    *chartInstance->c3_RI_mode = Isolated;
    break;

   default:
    covrtDecUpdateFcn(chartInstance->c3_covrtInstance, 4U, 17, 1, 0);
    *chartInstance->c3_RI_mode = Isolated;
    break;
  }
}

static void c3_b_enter_atomic_Active(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  int32_T c3_previousEvent;
  c3_previousEvent = chartInstance->c3_sfEvent;
  chartInstance->c3_sfEvent = c3_event_E;
  if (chartInstance->c3_is_active_RO != 0U) {
    c3_RO(chartInstance);
  }

  chartInstance->c3_sfEvent = c3_previousEvent;
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
  boolean_T c3_aVarTruthTableCondition_1;
  boolean_T c3_aVarTruthTableCondition_2;
  boolean_T c3_aVarTruthTableCondition_3;
  boolean_T c3_aVarTruthTableCondition_4;
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
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 9U, 0.0);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 10U, 0.0);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 11U, 0.0);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 12U, 0.0);
  chartInstance->c3_JITTransitionAnimation[52U] = 1U;
  chartInstance->c3_JITTransitionAnimation[53U] = 1U;
  c3_aVarTruthTableCondition_1 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[0];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 9U, (real_T)
                    c3_aVarTruthTableCondition_1);
  chartInstance->c3_JITTransitionAnimation[54U] = 1U;
  c3_aVarTruthTableCondition_2 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [16])[0];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 10U, (real_T)
                    c3_aVarTruthTableCondition_2);
  chartInstance->c3_JITTransitionAnimation[55U] = 1U;
  c3_aVarTruthTableCondition_3 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[1];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 11U, (real_T)
                    c3_aVarTruthTableCondition_3);
  chartInstance->c3_JITTransitionAnimation[56U] = 1U;
  c3_aVarTruthTableCondition_4 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [16])[1];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 12U, (real_T)
                    c3_aVarTruthTableCondition_4);
  c3_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 57U, 0,
    c3_aVarTruthTableCondition_1 != 0U);
  if (c3_temp) {
    c3_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 57U, 1,
      c3_aVarTruthTableCondition_3 != 0U);
  }

  c3_b_temp = c3_temp;
  if (c3_b_temp) {
    c3_b_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 57U, 2,
      c3_aVarTruthTableCondition_4 != 0U);
  }

  c3_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U, 57U,
    0U, c3_b_temp != 0U);
  if (c3_out) {
    chartInstance->c3_JITTransitionAnimation[57U] = 1U;
    chartInstance->c3_JITTransitionAnimation[58U] = 1U;
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_go_off;
    if (chartInstance->c3_is_active_LO != 0U) {
      c3_LO(chartInstance);
    }

    chartInstance->c3_sfEvent = c3_previousEvent;
  } else {
    chartInstance->c3_JITTransitionAnimation[59U] = 1U;
    c3_b_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
      60U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 60U, 0,
      c3_aVarTruthTableCondition_1 != 0U) != 0U);
    if (c3_b_out) {
      chartInstance->c3_JITTransitionAnimation[60U] = 1U;
      chartInstance->c3_JITTransitionAnimation[61U] = 1U;
      c3_b_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      if (chartInstance->c3_is_active_LO != 0U) {
        c3_LO(chartInstance);
      }

      chartInstance->c3_sfEvent = c3_b_previousEvent;
      chartInstance->c3_JITTransitionAnimation[62U] = 1U;
      c3_c_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      if (chartInstance->c3_is_active_LI != 0U) {
        c3_LI(chartInstance);
      }

      chartInstance->c3_sfEvent = c3_c_previousEvent;
    } else {
      chartInstance->c3_JITTransitionAnimation[63U] = 1U;
      c3_c_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 64U,
        0, c3_aVarTruthTableCondition_1 != 0U);
      if (c3_c_temp) {
        c3_c_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 64U,
          1, c3_aVarTruthTableCondition_2 != 0U);
      }

      c3_d_temp = c3_c_temp;
      if (c3_d_temp) {
        c3_d_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 64U,
          2, c3_aVarTruthTableCondition_3 != 0U);
      }

      c3_e_temp = c3_d_temp;
      if (c3_e_temp) {
        c3_e_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 64U,
          3, c3_aVarTruthTableCondition_4 != 0U);
      }

      c3_c_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
        64U, 0U, c3_e_temp != 0U);
      if (c3_c_out) {
        chartInstance->c3_JITTransitionAnimation[64U] = 1U;
        chartInstance->c3_JITTransitionAnimation[65U] = 1U;
        c3_d_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_go_isolated;
        if (chartInstance->c3_is_active_LO != 0U) {
          c3_LO(chartInstance);
        }

        chartInstance->c3_sfEvent = c3_d_previousEvent;
      } else {
        chartInstance->c3_JITTransitionAnimation[66U] = 1U;
        c3_f_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 67U,
          0, c3_aVarTruthTableCondition_1 != 0U);
        if (c3_f_temp) {
          c3_f_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            67U, 1, c3_aVarTruthTableCondition_2 != 0U);
        }

        c3_d_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 67U, 0U, c3_f_temp != 0U);
        if (c3_d_out) {
          chartInstance->c3_JITTransitionAnimation[67U] = 1U;
          chartInstance->c3_JITTransitionAnimation[68U] = 1U;
          c3_e_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          if (chartInstance->c3_is_active_LO != 0U) {
            c3_LO(chartInstance);
          }

          chartInstance->c3_sfEvent = c3_e_previousEvent;
          chartInstance->c3_JITTransitionAnimation[69U] = 1U;
          c3_h_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          if (chartInstance->c3_is_active_LI != 0U) {
            c3_LI(chartInstance);
          }

          chartInstance->c3_sfEvent = c3_h_previousEvent;
        } else {
          chartInstance->c3_JITTransitionAnimation[70U] = 1U;
          c3_e_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
            5U, 71U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            71U, 0, c3_aVarTruthTableCondition_3 != 0U) != 0U);
          if (c3_e_out) {
            chartInstance->c3_JITTransitionAnimation[71U] = 1U;
            chartInstance->c3_JITTransitionAnimation[72U] = 1U;
            c3_f_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_go_off;
            if (chartInstance->c3_is_active_LI != 0U) {
              c3_LI(chartInstance);
            }

            chartInstance->c3_sfEvent = c3_f_previousEvent;
          } else {
            chartInstance->c3_JITTransitionAnimation[73U] = 1U;
            c3_f_out = covrtTransitionDecUpdateFcn
              (chartInstance->c3_covrtInstance, 5U, 74U, 0U, covrtCondUpdateFcn
               (chartInstance->c3_covrtInstance, 5U, 74U, 0,
                c3_aVarTruthTableCondition_4 != 0U) != 0U);
            if (c3_f_out) {
              chartInstance->c3_JITTransitionAnimation[74U] = 1U;
              chartInstance->c3_JITTransitionAnimation[75U] = 1U;
              c3_g_previousEvent = chartInstance->c3_sfEvent;
              chartInstance->c3_sfEvent = c3_event_go_isolated;
              if (chartInstance->c3_is_active_LI != 0U) {
                c3_LI(chartInstance);
              }

              chartInstance->c3_sfEvent = c3_g_previousEvent;
            } else {
              chartInstance->c3_JITTransitionAnimation[76U] = 1U;
              chartInstance->c3_JITTransitionAnimation[77U] = 1U;
              chartInstance->c3_JITTransitionAnimation[78U] = 1U;
            }
          }
        }
      }
    }
  }
}

static void c3_R_switch(SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  boolean_T c3_aVarTruthTableCondition_1;
  boolean_T c3_aVarTruthTableCondition_2;
  boolean_T c3_aVarTruthTableCondition_3;
  boolean_T c3_aVarTruthTableCondition_4;
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
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 13U, 0.0);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 14U, 0.0);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 15U, 0.0);
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 16U, 0.0);
  chartInstance->c3_JITTransitionAnimation[79U] = 1U;
  chartInstance->c3_JITTransitionAnimation[80U] = 1U;
  c3_aVarTruthTableCondition_1 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[2];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 13U, (real_T)
                    c3_aVarTruthTableCondition_1);
  chartInstance->c3_JITTransitionAnimation[81U] = 1U;
  c3_aVarTruthTableCondition_2 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [40])[0];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 14U, (real_T)
                    c3_aVarTruthTableCondition_2);
  chartInstance->c3_JITTransitionAnimation[82U] = 1U;
  c3_aVarTruthTableCondition_3 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [72])[1];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 15U, (real_T)
                    c3_aVarTruthTableCondition_3);
  chartInstance->c3_JITTransitionAnimation[83U] = 1U;
  c3_aVarTruthTableCondition_4 = ((boolean_T *)&((char_T *)chartInstance->c3_u)
    [40])[1];
  covrtSigUpdateFcn(chartInstance->c3_covrtInstance, 16U, (real_T)
                    c3_aVarTruthTableCondition_4);
  c3_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 84U, 0,
    c3_aVarTruthTableCondition_1 != 0U);
  if (c3_temp) {
    c3_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 84U, 1,
      c3_aVarTruthTableCondition_3 != 0U);
  }

  c3_b_temp = c3_temp;
  if (c3_b_temp) {
    c3_b_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 84U, 2,
      c3_aVarTruthTableCondition_4 != 0U);
  }

  c3_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U, 84U,
    0U, c3_b_temp != 0U);
  if (c3_out) {
    chartInstance->c3_JITTransitionAnimation[84U] = 1U;
    chartInstance->c3_JITTransitionAnimation[85U] = 1U;
    c3_previousEvent = chartInstance->c3_sfEvent;
    chartInstance->c3_sfEvent = c3_event_go_off;
    if (chartInstance->c3_is_active_RO != 0U) {
      c3_RO(chartInstance);
    }

    chartInstance->c3_sfEvent = c3_previousEvent;
  } else {
    chartInstance->c3_JITTransitionAnimation[86U] = 1U;
    c3_b_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
      87U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 87U, 0,
      c3_aVarTruthTableCondition_1 != 0U) != 0U);
    if (c3_b_out) {
      chartInstance->c3_JITTransitionAnimation[87U] = 1U;
      chartInstance->c3_JITTransitionAnimation[88U] = 1U;
      c3_b_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      if (chartInstance->c3_is_active_RO != 0U) {
        c3_RO(chartInstance);
      }

      chartInstance->c3_sfEvent = c3_b_previousEvent;
      c3_c_previousEvent = chartInstance->c3_sfEvent;
      chartInstance->c3_sfEvent = c3_event_go_isolated;
      if (chartInstance->c3_is_active_RI != 0U) {
        c3_RI(chartInstance);
      }

      chartInstance->c3_sfEvent = c3_c_previousEvent;
    } else {
      chartInstance->c3_JITTransitionAnimation[89U] = 1U;
      c3_c_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 90U,
        0, c3_aVarTruthTableCondition_1 != 0U);
      if (c3_c_temp) {
        c3_c_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 90U,
          1, c3_aVarTruthTableCondition_2 != 0U);
      }

      c3_d_temp = c3_c_temp;
      if (c3_d_temp) {
        c3_d_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 90U,
          2, c3_aVarTruthTableCondition_3 != 0U);
      }

      c3_e_temp = c3_d_temp;
      if (c3_e_temp) {
        c3_e_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 90U,
          3, c3_aVarTruthTableCondition_4 != 0U);
      }

      c3_c_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance, 5U,
        90U, 0U, c3_e_temp != 0U);
      if (c3_c_out) {
        chartInstance->c3_JITTransitionAnimation[90U] = 1U;
        chartInstance->c3_JITTransitionAnimation[91U] = 1U;
        c3_d_previousEvent = chartInstance->c3_sfEvent;
        chartInstance->c3_sfEvent = c3_event_go_isolated;
        if (chartInstance->c3_is_active_RO != 0U) {
          c3_RO(chartInstance);
        }

        chartInstance->c3_sfEvent = c3_d_previousEvent;
      } else {
        chartInstance->c3_JITTransitionAnimation[92U] = 1U;
        c3_f_temp = !covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U, 93U,
          0, c3_aVarTruthTableCondition_1 != 0U);
        if (c3_f_temp) {
          c3_f_temp = covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            93U, 1, c3_aVarTruthTableCondition_2 != 0U);
        }

        c3_d_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
          5U, 93U, 0U, c3_f_temp != 0U);
        if (c3_d_out) {
          chartInstance->c3_JITTransitionAnimation[93U] = 1U;
          chartInstance->c3_JITTransitionAnimation[94U] = 1U;
          c3_e_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          if (chartInstance->c3_is_active_RO != 0U) {
            c3_RO(chartInstance);
          }

          chartInstance->c3_sfEvent = c3_e_previousEvent;
          c3_g_previousEvent = chartInstance->c3_sfEvent;
          chartInstance->c3_sfEvent = c3_event_go_isolated;
          if (chartInstance->c3_is_active_RI != 0U) {
            c3_RI(chartInstance);
          }

          chartInstance->c3_sfEvent = c3_g_previousEvent;
        } else {
          chartInstance->c3_JITTransitionAnimation[95U] = 1U;
          c3_e_out = covrtTransitionDecUpdateFcn(chartInstance->c3_covrtInstance,
            5U, 96U, 0U, covrtCondUpdateFcn(chartInstance->c3_covrtInstance, 5U,
            96U, 0, c3_aVarTruthTableCondition_3 != 0U) != 0U);
          if (c3_e_out) {
            chartInstance->c3_JITTransitionAnimation[96U] = 1U;
            chartInstance->c3_JITTransitionAnimation[97U] = 1U;
            c3_f_previousEvent = chartInstance->c3_sfEvent;
            chartInstance->c3_sfEvent = c3_event_go_off;
            if (chartInstance->c3_is_active_RI != 0U) {
              c3_RI(chartInstance);
            }

            chartInstance->c3_sfEvent = c3_f_previousEvent;
          } else {
            chartInstance->c3_JITTransitionAnimation[98U] = 1U;
            c3_f_out = covrtTransitionDecUpdateFcn
              (chartInstance->c3_covrtInstance, 5U, 99U, 0U, covrtCondUpdateFcn
               (chartInstance->c3_covrtInstance, 5U, 99U, 0,
                c3_aVarTruthTableCondition_4 != 0U) != 0U);
            if (c3_f_out) {
              chartInstance->c3_JITTransitionAnimation[99U] = 1U;
              chartInstance->c3_JITTransitionAnimation[100U] = 1U;
              c3_h_previousEvent = chartInstance->c3_sfEvent;
              chartInstance->c3_sfEvent = c3_event_go_isolated;
              if (chartInstance->c3_is_active_RI != 0U) {
                c3_RI(chartInstance);
              }

              chartInstance->c3_sfEvent = c3_h_previousEvent;
            } else {
              chartInstance->c3_JITTransitionAnimation[101U] = 1U;
              chartInstance->c3_JITTransitionAnimation[102U] = 1U;
              chartInstance->c3_JITTransitionAnimation[103U] = 1U;
            }
          }
        }
      }
    }
  }
}

static sf_aircraft_ModeType c3_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray
   *c3_b_LI_mode, const char_T *c3_identifier)
{
  sf_aircraft_ModeType c3_y;
  emlrtMsgIdentifier c3_thisId;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_b_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_b_LI_mode),
    &c3_thisId);
  sf_mex_destroy(&c3_b_LI_mode);
  return c3_y;
}

static sf_aircraft_ModeType c3_b_emlrt_marshallIn
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, const mxArray *c3_b_u,
   const emlrtMsgIdentifier *c3_parentId)
{
  sf_aircraft_ModeType c3_y;
  (void)chartInstance;
  sf_mex_check_enum("sf_aircraft_ModeType", 5, c3_sv, c3_iv);
  sf_mex_check_builtin(c3_parentId, c3_b_u, "sf_aircraft_ModeType", 0, 0U, NULL);
  c3_y = (sf_aircraft_ModeType)sf_mex_get_enum_element(c3_b_u, 0);
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static int32_T c3_c_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_e_fails, const char_T *c3_identifier)
{
  int32_T c3_y;
  emlrtMsgIdentifier c3_thisId;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_d_emlrt_marshallIn(chartInstance, sf_mex_dup(c3_e_fails), &c3_thisId);
  sf_mex_destroy(&c3_e_fails);
  return c3_y;
}

static int32_T c3_d_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId)
{
  int32_T c3_y;
  int32_T c3_i;
  (void)chartInstance;
  sf_mex_import(c3_parentId, sf_mex_dup(c3_b_u), &c3_i, 1, 6, 0U, 0, 0U, 0);
  c3_y = c3_i;
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static uint8_T c3_e_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_is_active_c3_sf_aircraft_fault, const
  char_T *c3_identifier)
{
  uint8_T c3_y;
  emlrtMsgIdentifier c3_thisId;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  c3_y = c3_f_emlrt_marshallIn(chartInstance, sf_mex_dup
    (c3_b_is_active_c3_sf_aircraft_fault), &c3_thisId);
  sf_mex_destroy(&c3_b_is_active_c3_sf_aircraft_fault);
  return c3_y;
}

static uint8_T c3_f_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_u, const emlrtMsgIdentifier *c3_parentId)
{
  uint8_T c3_y;
  uint8_T c3_c_u;
  (void)chartInstance;
  sf_mex_import(c3_parentId, sf_mex_dup(c3_b_u), &c3_c_u, 1, 3, 0U, 0, 0U, 0);
  c3_y = c3_c_u;
  sf_mex_destroy(&c3_b_u);
  return c3_y;
}

static const mxArray *c3_g_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance, const mxArray *c3_b_setSimStateSideEffectsInfo, const char_T
  *c3_identifier)
{
  const mxArray *c3_y = NULL;
  emlrtMsgIdentifier c3_thisId;
  c3_y = NULL;
  c3_thisId.fIdentifier = (const char *)c3_identifier;
  c3_thisId.fParent = NULL;
  c3_thisId.bParentIsCell = false;
  sf_mex_assign(&c3_y, c3_h_emlrt_marshallIn(chartInstance, sf_mex_dup
    (c3_b_setSimStateSideEffectsInfo), &c3_thisId), false);
  sf_mex_destroy(&c3_b_setSimStateSideEffectsInfo);
  return c3_y;
}

static const mxArray *c3_h_emlrt_marshallIn(SFc3_sf_aircraft_faultInstanceStruct
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

static void c3_slStringInitializeDynamicBuffers
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void c3_init_sf_message_store_memory(SFc3_sf_aircraft_faultInstanceStruct
  *chartInstance)
{
  (void)chartInstance;
}

static const mxArray *c3_chart_data_browse_helper
  (SFc3_sf_aircraft_faultInstanceStruct *chartInstance, int32_T c3_ssIdNumber)
{
  const mxArray *c3_mxData = NULL;
  const mxArray *c3_m = NULL;
  sf_aircraft_ModeType c3_r;
  sf_aircraft_ModeType c3_r1;
  sf_aircraft_ModeType c3_r2;
  sf_aircraft_ModeType c3_r3;
  const mxArray *c3_m1 = NULL;
  int32_T c3_i;
  int32_T c3_i1;
  int32_T c3_i2;
  int32_T c3_i3;
  const mxArray *c3_m2 = NULL;
  const mxArray *c3_m3 = NULL;
  const mxArray *c3_m4 = NULL;
  c3_mxData = NULL;
  switch (c3_ssIdNumber) {
   case 460U:
    c3_m = NULL;
    sf_mex_assign(&c3_m, sf_mex_createstruct("mxData", 0, NULL, 0), false);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (real_T *)&((char_T *)
      chartInstance->c3_u)[0], 0, 0U, 1U, 0U, 1, 2), "L_pos", "mxData", 0);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (boolean_T *)&((char_T *)
      chartInstance->c3_u)[16], 11, 0U, 1U, 0U, 1, 2), "L_pos_fail", "mxData", 0);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (real_T *)&((char_T *)
      chartInstance->c3_u)[24], 0, 0U, 1U, 0U, 1, 2), "R_pos", "mxData", 0);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (boolean_T *)&((char_T *)
      chartInstance->c3_u)[40], 11, 0U, 1U, 0U, 1, 2), "R_pos_fail", "mxData", 0);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (real_T *)&((char_T *)
      chartInstance->c3_u)[48], 0, 0U, 0U, 0U, 0), "H1_press", "mxData", 0);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (real_T *)&((char_T *)
      chartInstance->c3_u)[56], 0, 0U, 0U, 0U, 0), "H2_press", "mxData", 0);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (real_T *)&((char_T *)
      chartInstance->c3_u)[64], 0, 0U, 0U, 0U, 0), "H3_press", "mxData", 0);
    sf_mex_addfield(c3_m, sf_mex_create("mxData", (boolean_T *)&((char_T *)
      chartInstance->c3_u)[72], 11, 0U, 1U, 0U, 1, 3), "low_press", "mxData", 0);
    sf_mex_assign(&c3_mxData, c3_m, false);
    break;

   case 918U:
    c3_r = *chartInstance->c3_LO_mode;
    c3_i = (int32_T)c3_r;
    sf_mex_assign(&c3_m1, sf_mex_create("unnamed temp", &c3_i, 6, 0U, 0U, 0U, 0),
                  false);
    sf_mex_assign(&c3_mxData, sf_mex_create_enum("sf_aircraft_ModeType", c3_m1),
                  false);
    break;

   case 919U:
    c3_r1 = *chartInstance->c3_RO_mode;
    c3_i1 = (int32_T)c3_r1;
    sf_mex_assign(&c3_m2, sf_mex_create("unnamed temp", &c3_i1, 6, 0U, 0U, 0U, 0),
                  false);
    sf_mex_assign(&c3_mxData, sf_mex_create_enum("sf_aircraft_ModeType", c3_m2),
                  false);
    break;

   case 920U:
    c3_r2 = *chartInstance->c3_LI_mode;
    c3_i2 = (int32_T)c3_r2;
    sf_mex_assign(&c3_m3, sf_mex_create("unnamed temp", &c3_i2, 6, 0U, 0U, 0U, 0),
                  false);
    sf_mex_assign(&c3_mxData, sf_mex_create_enum("sf_aircraft_ModeType", c3_m3),
                  false);
    break;

   case 921U:
    c3_r3 = *chartInstance->c3_RI_mode;
    c3_i3 = (int32_T)c3_r3;
    sf_mex_assign(&c3_m4, sf_mex_create("unnamed temp", &c3_i3, 6, 0U, 0U, 0U, 0),
                  false);
    sf_mex_assign(&c3_mxData, sf_mex_create_enum("sf_aircraft_ModeType", c3_m4),
                  false);
    break;

   case 212U:
    sf_mex_assign(&c3_mxData, sf_mex_create("mxData", &chartInstance->c3_fails,
      6, 0U, 0U, 0U, 0), false);
    break;

   case 213U:
    sf_mex_assign(&c3_mxData, sf_mex_create("mxData", &chartInstance->c3_b_fails,
      6, 0U, 0U, 0U, 0), false);
    break;

   case 214U:
    sf_mex_assign(&c3_mxData, sf_mex_create("mxData", &chartInstance->c3_c_fails,
      6, 0U, 0U, 0U, 0), false);
    break;

   case 215U:
    sf_mex_assign(&c3_mxData, sf_mex_create("mxData", &chartInstance->c3_d_fails,
      6, 0U, 0U, 0U, 0), false);
    break;
  }

  sf_mex_destroy(&c3_m1);
  sf_mex_destroy(&c3_m2);
  sf_mex_destroy(&c3_m3);
  sf_mex_destroy(&c3_m4);
  return c3_mxData;
}

static int32_T c3__s32_add__(SFc3_sf_aircraft_faultInstanceStruct *chartInstance,
  int32_T c3_b, int32_T c3_c, int32_T c3_EMLOvCount_src_loc, uint32_T
  c3_ssid_src_loc, int32_T c3_offset_src_loc, int32_T c3_length_src_loc)
{
  int32_T c3_a;
  (void)c3_EMLOvCount_src_loc;
  c3_a = c3_b + c3_c;
  if (((c3_a ^ c3_b) & (c3_a ^ c3_c)) < 0) {
    sf_data_overflow_error(chartInstance->S, c3_ssid_src_loc, c3_offset_src_loc,
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
  chartInstance->c3_covrtInstance = (CovrtStateflowInstance *)
    sfrtGetCovrtInstance(chartInstance->S);
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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* SFunction Glue Code */
void sf_c3_sf_aircraft_fault_get_check_sum(mxArray *plhs[])
{
  ((real_T *)mxGetPr((plhs[0])))[0] = (real_T)(2915793234U);
  ((real_T *)mxGetPr((plhs[0])))[1] = (real_T)(232768780U);
  ((real_T *)mxGetPr((plhs[0])))[2] = (real_T)(3079908584U);
  ((real_T *)mxGetPr((plhs[0])))[3] = (real_T)(4192461941U);
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

static const mxArray *sf_get_sim_state_info_c3_sf_aircraft_fault(void)
{
  const char *infoFields[] = { "chartChecksum", "varInfo" };

  mxArray *mxInfo = mxCreateStructMatrix(1, 1, 2, infoFields);
  mxArray *mxVarInfo = sf_mex_decode(
    "eNpjYPT0ZQACPiDeACTYgDQHEDMxQAArlM8IxEJQGiLOAhdXAOKSyoJUkHhxUbJnCpDOS8wF8xN"
    "LKzzz0vLB5lswIMxnw2I+I5L5nFBxKHCgSP+BHgz9LFj0syPpF4DyfTzjc/NTUsHuh4XTgPljAw"
    "X+8B9E/jhBvj+CBlN87KDAH1SNDw7K/NGQRZQ/WNH8AeKnJWbmFEPdP+D+WDBM/HFgmPjjwWDxh"
    "4IDheUE2P4AAv6QQ/MHiJ9ZHJ+YXJJZlhqfbBxfnBafmFmUXJSYVhKflliaUzJY/CcA1u9AwH88"
    "aP7jQfGfjz/DoIkvPSr4J2gQ+ceMGvHjOXj8Y0uN+KGif5SoUj54EPCPOJp/xCH+wVowDA5/CZB"
    "dfgP9BS4QBoc/9CjxR9Dg8YcZRfHhOWj8YUtRfCD7AwDdLX0a"
    );
  mxArray *mxChecksum = mxCreateDoubleMatrix(1, 4, mxREAL);
  sf_c3_sf_aircraft_fault_get_check_sum(&mxChecksum);
  mxSetField(mxInfo, 0, infoFields[0], mxChecksum);
  mxSetField(mxInfo, 0, infoFields[1], mxVarInfo);
  return mxInfo;
}

static const char* sf_get_instance_specialization(void)
{
  return "ssfOuq1tq5V0V2yrSopqQ8E";
}

static void sf_opaque_initialize_c3_sf_aircraft_fault(void *chartInstanceVar)
{
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

  sf_warn_if_symbolic_dimension_param_changed(S);
  if (sf_machine_global_initializer_called()) {
    initialize_params_c3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
      sf_get_chart_instance_ptr(S));
    initSimStructsc3_sf_aircraft_fault((SFc3_sf_aircraft_faultInstanceStruct*)
      sf_get_chart_instance_ptr(S));
  }
}

const char* sf_c3_sf_aircraft_fault_get_post_codegen_info(void)
{
  int i;
  const char* encStrCodegen [19] = {
    "eNrtmM9v3EQUx71RWlophBUXLlVVlQOcqgKi6qUoZH8ISxs2rJNwXCb283rY8YwzPzbJAYneK/E",
    "vIPEP9NBDj70gcUXixIl/gxvPXm+y9dreZL2AVbDkOOP9vjfvM+/5+YfVsPcs3LZxf3zHsm7i8R",
    "buG9Z0u5GOG3P79Pym9UE6/glF3IT7RJJQWaUbJyEMQAlmNBXc5r7IlVHugwTuojYSUhd5UzQ0j",
    "PJx13A39qe+DqgbOIEwzNtFW+L1OTtHb5HR++inTSW4ugvg6UAKMwq6jIwuIpb6tBWAO1YmLENQ",
    "oB0TxWGpPcM0jRh0zsC1udIEI1aXsTmaaGjps0LMmFQ5M6EII0YJz6UNiHIgwgXWcBh5+LdvNEJ",
    "lZW5ApN6FgExA9eg48Sk4ZH1ShT8cU060kJSwTshaseFibPsM49kTHrCSBcHYdiWQcSQo18X5d7",
    "pI2uHkmEEbjs2o2JsDJyZO/hGFU5CF6+a3xAQkGUGfF06aLEjnLMnWRZUsyjQN4YjIz13MnwKvs",
    "HqxcpRDME9wgBZFMkggbXUg6QSXt9CbCe24MpddMiacJlstkyXeOhMoy8KFt67LW4QxVSg7EFEP",
    "JsASr22iSbls6jVfF0kRkRFWrYeLHJd4S3CPLuTCNUqLsIXl1u71vsROkR/cpczmGqRPXMi7bpU",
    "bgGcYICh2Jp1Ml+PUoyrO1hJVmtNlKkv5hrdPhRwjaMllf4kQ56BQGKoRrj7W7qHCMi+Txau/VD",
    "fr8w+tyz6/dYU+P7PLHj+c89PI8WPNHbPz3t4on3cD/2ukdjtzdm9n5tnM2MW6Ju5/DuDws99//",
    "uH+0/eHv3334tcq83/zzvXui9vp+M6sAV2U52ShKmLtF3Nxbeb4f2/OfzMdK+X3zclH+uTTo4dH",
    "H59LR0QnXz3uJP6eb5fH+24m3tn5e3EnPI+Svqaka3vpDTseEzO9jSXPCXPx3lyyHrfT8+m2U8n",
    "+1bMF+7z1eiuzXvG4Zw9DvNxeq99/jeN5BY5+jTh+WZ1jUKd8vKzAsdZ83KrG8f23V+K4keGIxz",
    "6hybNALTh+fEM4Xr0hHH/UhePeTsU+kcy/v4TjbobjbvK+MST49jCBofvJUPlDQqUria+HPsGXw",
    "LrwNXeyz0t5fFsZvq3X+Hp9qzb5erAGnkGNeB6tIz92fXierCM/a+S5v5b+sMrzOPLkNoZ6cDVX",
    "7t/IlTSEenA8qMIxqA/Ho0r5sGvD8aRSPrIcq76fX9fO+t+uFnaN/yDfVb63rWq3WfH73j9lV5X",
    "vut8dq3ynzPYzK6NvVpjn79ZX/V57Hf1fg/DCdg==",
    ""
  };

  static char newstr [1317] = "";
  newstr[0] = '\0';
  for (i = 0; i < 19; i++) {
    strcat(newstr, encStrCodegen[i]);
  }

  return newstr;
}

static void mdlSetWorkWidths_c3_sf_aircraft_fault(SimStruct *S)
{
  const char* newstr = sf_c3_sf_aircraft_fault_get_post_codegen_info();
  sf_set_work_widths(S, newstr);
  ssSetChecksum0(S,(1432703737U));
  ssSetChecksum1(S,(2412108350U));
  ssSetChecksum2(S,(1596162338U));
  ssSetChecksum3(S,(3518266836U));
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
  chartInstance->chartInfo.callGetHoverDataForMsg = NULL;
  chartInstance->chartInfo.extModeExec = NULL;
  chartInstance->chartInfo.restoreLastMajorStepConfiguration = NULL;
  chartInstance->chartInfo.restoreBeforeLastMajorStepConfiguration = NULL;
  chartInstance->chartInfo.storeCurrentConfiguration = NULL;
  chartInstance->chartInfo.callAtomicSubchartUserFcn = NULL;
  chartInstance->chartInfo.callAtomicSubchartAutoFcn = NULL;
  chartInstance->chartInfo.callAtomicSubchartEventFcn = NULL;
  chartInstance->S = S;
  chartInstance->chartInfo.dispatchToExportedFcn = NULL;
  sf_init_ChartRunTimeInfo(S, &(chartInstance->chartInfo), false, 0,
    chartInstance->c3_JITStateAnimation,
    chartInstance->c3_JITTransitionAnimation);
  init_dsm_address_info(chartInstance);
  init_simulink_io_address(chartInstance);
  if (!sim_mode_is_rtw_gen(S)) {
  }

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
