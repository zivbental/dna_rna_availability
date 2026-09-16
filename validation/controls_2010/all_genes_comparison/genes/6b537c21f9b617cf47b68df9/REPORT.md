# YNL189W
Status: ok. Length: 1951 nt. Measured usable bases: 1470. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1470 | 0.3031 | 0.2891 |
| rnafold | ok | 1470 | 0.2776 | 0.2836 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1123 | -0.0189 | 0.0093 |
| seed_p | 1123 | -0.1007 | -0.0579 |
| seed_p_vs_seed_pars | 875 | -0.2968 | -0.2707 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
