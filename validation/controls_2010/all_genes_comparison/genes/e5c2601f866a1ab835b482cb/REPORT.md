# YNL049C
Status: ok. Length: 2757 nt. Measured usable bases: 1331. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1331 | 0.3351 | 0.3326 |
| rnafold | ok | 1331 | 0.2941 | 0.2858 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 256 | -0.3240 | -0.4252 |
| seed_p | 256 | -0.5414 | -0.4994 |
| seed_p_vs_seed_pars | 180 | -0.5283 | -0.5087 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
