| No. | Formula                                                                   | Name                                        |
| --- | ------------------------------------------------------------------------- | ------------------------------------------- |
| 1   | $d(x, \xi) = \sum_{i=1}^{N} [\xi_i(1 - x_i) + (1 - \xi_i)x_i]$            | **Hamming Distance**                        |
| 2   | $O_i(t+1) = \text{sgn}\left( \sum_j w_{ij} O_j(t) \right)$                | **Update Rule**                             |
| 3   | $w_{ij} = \frac{1}{N} \xi_i \xi_j$                                        | **Single Pattern Weight Rule**              |
| 4   | $O_i = \text{sgn}\left( \sum_{j=1}^N w_{ij} \xi_j \right) = \xi_i$        | **Stability Condition (Single Pattern)**    |
| 5   | $w_{ij} = \frac{1}{N} \sum_{\mu=1}^P \xi_i^\mu \xi_j^\mu$                 | **Hebbian Rule (Multiple Patterns)**        |
| 6   | $h_i^\nu = \sum_j w_{ij} \xi_j^\nu = \xi_i^\nu + A$                       | **Stability Condition (Multiple Patterns)** |
| 7   | $A = \frac{1}{N} \sum_{\mu \ne \nu} \xi_i^\mu \sum_j \xi_j^\mu \xi_j^\nu$ | **Crosstalk Term**                          |
| 8   | $C_i^\nu = 1 - \xi_i^\nu h_i^\nu$                                         | **Crosstalk Rewritten**                     |
| 9   | $P_{\text{error}} = \text{Prob}(C_i^\nu > 1)$                             | **Probability of Retrieval Error**          |
| 10  | $H = -\frac{1}{2} \sum_{i,j} w_{ij} x_i x_j$                              | **Energy Function**                         |
