# YPL094C
Status: ok. Length: 881 nt. Measured usable bases: 693. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 693 | 0.2150 | 0.2105 |
| rnafold | ok | 693 | 0.1825 | 0.1801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 573 | -0.2693 | 0.0273 |
| seed_p | 573 | -0.1212 | -0.0481 |
| seed_p_vs_seed_pars | 525 | -0.2612 | -0.1471 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
