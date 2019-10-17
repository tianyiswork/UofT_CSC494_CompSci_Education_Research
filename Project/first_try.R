s1 <- read.csv('s1.csv')

# let's try removing any subject who took 20 or more tries on either pre or post

s1 <- s1[s1$S1_pre < 20,]
s1 <- s1[s1$S1_post <20,]

control <- s1[s1$Group.ID == 'group_001',]
explain <- s1[s1$Group.ID == 'group_002',]
motivate <- s1[s1$Group.ID == 'group_003',]


treated <- rbind(explain, motivate)
t.test(control$S1_post, treated$S1_post)

# was there a difference pre-post for everyone 
print(t.test(s1$S1_pre, s1$S1_post, paired=TRUE))
