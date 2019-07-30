ab,cd=map(int,input().split())
ef,gh=map(int,input().split())
ij,kl=map(int,input().split())
if ab==cd and ef==gh and ij==kl:
	print("yes")
elif ab==ef and ab==ij:
	print("yes")
elif cd==gh and cd==kl:
	print("yes")
else:
	print("no")
