#!/usr/bin/python
import sys
def scoreAUC(labels,probs):
    i_sorted = sorted(range(len(probs)),key=lambda i: probs[i],
                      reverse=True)
    auc_temp = 0.0
    TP = 0.0
    TP_pre = 0.0
    FP = 0.0
    FP_pre = 0.0
    P = 0;
    N = 0;
    last_prob = probs[i_sorted[0]] + 1.0
    for i in range(len(probs)):
        if last_prob != probs[i_sorted[i]]: 
            auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0        
            TP_pre = TP
            FP_pre = FP
            last_prob = probs[i_sorted[i]]
	if labels[i_sorted[i]] == 1:
	    TP = TP + 1
	else:
	    FP = FP + 1
    auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0
    auc = auc_temp / (TP * FP)
    return auc
def read_file():
    labels = []
    probs = []
    for line in sys.stdin:
        line = line.strip().split()
        try:
            label = int(line[0])
            prob = float(line[1])
        except ValueError:
            # skip over header
            continue
        labels.append(label)
       	probs.append(prob)
    return (labels, probs)


def main():
    import sys
    labels, probs = read_file()
    auc = scoreAUC(labels, probs)
    print("AUC  : %f" % auc)

if __name__=="__main__":
    main()
