# YMR122W-A
Status: ok. Length: 547 nt. Measured usable bases: 457. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 457 | 0.1755 | 0.1926 |
| rnafold | ok | 457 | 0.1705 | 0.1909 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 409 | -0.0874 | -0.0546 |
| seed_p | 409 | -0.2584 | -0.1874 |
| seed_p_vs_seed_pars | 392 | -0.1521 | -0.1215 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
