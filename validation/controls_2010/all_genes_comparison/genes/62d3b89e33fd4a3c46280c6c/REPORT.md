# YDL126C
Status: ok. Length: 2607 nt. Measured usable bases: 2174. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2174 | 0.3196 | 0.3198 |
| rnafold | ok | 2174 | 0.2288 | 0.2312 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1953 | -0.0648 | -0.0346 |
| seed_p | 1953 | -0.2693 | -0.2182 |
| seed_p_vs_seed_pars | 1677 | -0.3463 | -0.3171 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
