# YLL039C
Status: ok. Length: 1353 nt. Measured usable bases: 577. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 577 | 0.3826 | 0.3800 |
| rnafold | ok | 577 | 0.3391 | 0.3410 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 286 | 0.0038 | -0.1804 |
| seed_p | 286 | 0.0190 | 0.0135 |
| seed_p_vs_seed_pars | 236 | -0.1758 | -0.1806 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
