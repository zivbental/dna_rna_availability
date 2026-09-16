# YCL057C-A
Status: ok. Length: 420 nt. Measured usable bases: 307. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 307 | 0.3003 | 0.2969 |
| rnafold | ok | 307 | 0.3035 | 0.2881 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | -0.4504 | -0.4263 |
| seed_p | 246 | -0.5286 | -0.4710 |
| seed_p_vs_seed_pars | 206 | -0.4557 | -0.3936 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
