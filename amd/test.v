已知counter_incr_pre=20,perfcounter_q=0, i_perfcounter_ne_zero_2=1,incr_one=1,incr_zero=0,spm_mode=`PERFMON_SPM_MODE_32BIT_CLAMP
如果counter_mode=`PERFMON_COUNTER_MODE_CYCLES_SINCE_FIRST_EVENT,   counter_incr=1


always @*
begin
case (counter_mode)
          `PERFMON_COUNTER_MODE_ACCUM,
          `PERFMON_COUNTER_MODE_MAX,
          `PERFMON_COUNTER_MODE_SAMPLE:
              counter_incr = counter_incr_pre;
          `PERFMON_COUNTER_MODE_ACTIVE_CYCLES,
          `PERFMON_COUNTER_MODE_INACTIVE_CYCLES,
          `PERFMON_COUNTER_MODE_DIRTY:
             counter_incr = ((|counter_incr_pre) ^ (counter_mode == `PERFMON_COUNTER_MODE_INACTIVE_CYCLES)) ? incr_one : incr_zero;
          `PERFMON_COUNTER_MODE_CYCLES_SINCE_FIRST_EVENT,
          `PERFMON_COUNTER_MODE_CYCLES_SINCE_LAST_EVENT:
             counter_incr = ((spm_mode == `PERFMON_SPM_MODE_OFF) ? (o_perfcounter_ne_zero | i_perfcounter_ne_zero_1 | i_perfcounter_ne_zero_2 | i_perfcounter_ne_zero_3) : (|perfcounter_q))
                                    ? incr_one : (|counter_incr_pre) ? incr_one : incr_zero;
          `PERFMON_COUNTER_MODE_CYCLES_GE_HI:
             counter_incr = incr_ge_counter ? incr_one : incr_zero;
          `PERFMON_COUNTER_MODE_CYCLES_EQ_HI:
            counter_incr = (counter_incr_pre == perfcounter_q[CNTR_WIDTH-1 : CNTR_WIDTH/2]) ? incr_one : incr_zero;
          default: counter_incr = counter_incr_pre;
       endcase // case(counter_mode)
end // always @ *
