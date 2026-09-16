# YIR008C
Status: ok. Length: 1286 nt. Measured usable bases: 606. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 606 | 0.2968 | 0.2703 |
| rnafold | ok | 606 | 0.1996 | 0.2065 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | -0.3022 | -0.1961 |
| seed_p | 68 | -0.2309 | -0.1305 |
| seed_p_vs_seed_pars | 57 | 0.2197 | 0.1149 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
