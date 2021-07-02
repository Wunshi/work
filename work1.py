# %%
import random
alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alpha_length=len(alpha)-1
def promote_code (num,length):
    for i in range(num):
        code=[]
        for j in range(length):
            n=random.randint(0,alpha_length)
            code.append(alpha[n])
            j+=1
        i+=1;j=0
        code_print="".join(code)
        print("The activation code for customer No.%d is %s."%(i,code_print))

if __name__ == "__main__":
    promote_code (200,5)

