t_data <- read.csv('w9_output.csv')

# let's try removing any subject who took 20 or more tries on either pre or post

#t_data <- t_data[t_data$S1_pre < 15,]
#t_data <- t_data[t_data$S1_post <15,]
#mt_data <- t_data[t_data$S2_post <15,]

control <- t_data[t_data$GID == '1',]
explain <- t_data[t_data$GID == '2',]
motivate <- t_data[t_data$GID == '3',]

treated <- rbind(explain, motivate)

s1_pre <- rowMeans(t_data[c('s1_pre1','s1_pre2_1','s1_pre2_2','s1_pre2_3','s1_pre2_4','s1_pre2_5')], na.rm=TRUE)
s1_pre2 <- rowMeans(t_data[c('s1_pre2_1','s1_pre2_2','s1_pre2_3','s1_pre2_4','s1_pre2_5')], na.rm=TRUE)


#t.test(control$s1_post, treated$s1_post)

# was there a difference pre-post for everyone 
#t.test(t_data$s1_pre, t_data$s1_post, paired=TRUE)

