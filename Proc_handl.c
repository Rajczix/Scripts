#include <sys/types.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>


#define MAX 100

int main (){
int z;
char b[1];
FILE *u;
FILE *un;       
 FILE *p; 
char lo[MAX];	
char ll[MAX];
        char buf[5];
        char k[1];
        char ia[MAX];      
	while(1){
		int child=0;
		char polecenie[1];
	
	int status=0;
		printf("Podaj polecenie do wykonania [u,s,c,e,q]:\n");
        	fgets(buf, sizeof(buf), stdin);
		sscanf(buf, "%s", polecenie);
                child=fork();
		switch(child){
		case -1:
			exit(1);
			break;
		case 0: 
			if(child==0){
            		printf("\nTu potomek pid=%d\n\n", getpid());
            		/*...wykonanie polecenia potomka...*/
			switch (polecenie[0]) {
      				case 'u':
                                      u=popen("uname -n","r");
while ( fgets(ll, MAX, u) != NULL){
fputs(ll,stdin);
}
un=popen("uname","r");
while(fgets( lo,MAX,un) != NULL){
fputs(lo,stdin);
}
printf("To jest komputer %s system operacyjny %s",ll,lo);
pclose(u); pclose(un);                                                                               
					break; 

				case 's':
					execlp("sh","sh",NULL);
					break;
				case 'c':
					
       execlp("xclock","xclock", "-a", "-update","1", NULL);
					break;
				case 'e':
        p=popen("zenity --file-selection","r");
      while ( fgets(ia, MAX, p) != NULL ){
fputs(ia, stdin);
}
sscanf(ia, "%s", k);
printf("%d",sizeof(k));

execlp("xedit","xedit", k,  NULL);
pclose(p);       		
					break;

				case 'q':
					exit(0);			
					break;
            			}
			exit(0); 
    			break;
			}
        	default:
			printf("Tu rodzic po utworzeniu potomka.\n");
        		

switch (polecenie[0])
{
case 'u':
waitpid(child,&status,0);
system("echo ");
break;
case 's':
waitpid(child,&status,0);
system("echo ");
break;
case 'q':
waitpid(child,&status,0);
exit(0);
break;
}

       		while (1){
                      z = waitpid(0,NULL,WNOHANG);
if (z <= 0)
{
break;
}
}
system("echo ");


		} 
	}

}


