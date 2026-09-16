# YMR220W
Status: ok. Length: 1519 nt. Measured usable bases: 961. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 961 | 0.2932 | 0.2716 |
| rnafold | ok | 961 | 0.2271 | 0.2423 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 420 | -0.3143 | -0.0533 |
| seed_p | 420 | -0.4914 | -0.2894 |
| seed_p_vs_seed_pars | 328 | -0.5641 | -0.5229 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
