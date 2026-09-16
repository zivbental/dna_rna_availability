# YML100W
Status: ok. Length: 3462 nt. Measured usable bases: 1837. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1837 | 0.2721 | 0.2521 |
| rnafold | ok | 1837 | 0.2367 | 0.2249 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 408 | -0.1733 | -0.2186 |
| seed_p | 408 | -0.2202 | -0.1594 |
| seed_p_vs_seed_pars | 327 | -0.2475 | -0.1830 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
