# YLR447C
Status: ok. Length: 1216 nt. Measured usable bases: 963. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 963 | 0.2844 | 0.2660 |
| rnafold | ok | 963 | 0.2439 | 0.2137 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 837 | 0.0803 | -0.0856 |
| seed_p | 837 | -0.0526 | -0.0431 |
| seed_p_vs_seed_pars | 718 | -0.0268 | -0.1105 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
