# YGR197C
Status: ok. Length: 1733 nt. Measured usable bases: 596. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 596 | 0.3120 | 0.2744 |
| rnafold | ok | 596 | 0.1733 | 0.1646 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | -0.1383 | 0.0188 |
| seed_p | 45 | -0.5910 | -0.6498 |
| seed_p_vs_seed_pars | 25 | -0.9703 | -0.9695 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
