# Graph Partitioning Enhancement in Relational Cloud
In this project we first model a single table from a relational database into a graph, then we partition this single graph into known number of partitions. We use both horizontal and vertical partitioning in order to find natural relations between __chunks__ of data.

Relational Cloud is refer to a kind of distributed database system that is relational. We use [Jabe-Ja](http://www.sics.se/~fatemeh/files/papers/jabeja.pdf) graph partitioning algorithm in this project which is a kind used to partition social media modeled graphs.

## Data-set
We use two kinds of data:

1. One big relational database table from one of the known social networks.
2. Test queries into that database.

## Keywords
Distributed Database System - Graph Partitioning - Database Graph Modeling - Database as a Service

## Installation
After cloning this repository, you'll have to install it's dependencies.

```bash
pip install networkx
```

# References
1. [Rountree, Derrick, and Ileana Castrillo. The basics of cloud computing: Understanding the fundamentals of cloud computing in theory and practice. Newnes, 2013.](https://books.google.com/books?hl=en&lr=&id=k7gwl2jgBBwC&oi=fnd&pg=PP1&dq=Rountree,+Derrick,+and+Ileana+Castrillo.+The+Basics+of+Cloud+Computing:+Understanding+the+Fundamentals+of+Cloud+Computing+in+Theory+and+Practice.+Newnes,+2013.&ots=Q9u_TTi0yH&sig=ph9Ew3k34JqzyN43CKe6ts93UVw)
2. [Giriraj, M., and S. Muthu. "From Cloud Computing to Cloud Manufacturing Excution Assembly System." Trends in Intelligent Robotics, Automation, and Manufacturing. Springer Berlin Heidelberg, 2012. 303-312.](http://link.springer.com/chapter/10.1007/978-3-642-35197-6_34)
3. [Curino, Carlo, et al. "Relational cloud: A database-as-a-service for the cloud." (2011).](http://dspace.mit.edu/handle/1721.1/62241)
4. [Curino, Carlo, et al. "Schism: a workload-driven approach to database replication and partitioning." Proceedings of the VLDB Endowment 3.1-2 (2010): 48-57.](http://dl.acm.org/citation.cfm?id=1920853)
5. [Karypis, George, and Vipin Kumar. "Multilevelk-way partitioning scheme for irregular graphs." Journal of Parallel and Distributed computing 48.1 (1998): 96-129.](http://www.sciencedirect.com/science/article/pii/S0743731597914040)
6. [Karypis, George, and Vipin Kumar. "A fast and high quality multilevel scheme for partitioning irregular graphs." SIAM Journal on scientific Computing 20.1 (1998): 359-392.](http://epubs.siam.org/doi/abs/10.1137/S1064827595287997)
7. [Rahimian, Fatemeh, et al. "Ja-be-ja: A distributed algorithm for balanced graph partitioning." (2013).](http://soda.swedish-ict.se/5473/)
8. [Rahimian, Fatemeh, et al. "Distributed vertex-cut partitioning." IFIP International Conference on Distributed Applications and Interoperable Systems. Springer Berlin Heidelberg, 2014.](http://link.springer.com/chapter/10.1007/978-3-662-43352-2_15)
9. [Rahimian, Fatemeh, et al. "A distributed algorithm for large-scale graph partitioning." ACM Transactions on Autonomous and Adaptive Systems (TAAS) 10.2 (2015): 12.](http://dl.acm.org/citation.cfm?id=2714568)

