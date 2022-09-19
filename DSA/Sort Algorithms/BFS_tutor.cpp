#include <stdio.h>
#define VISITED 1
#define UNVISITED 0
#define VALID 1
#define INVALID 0
#define WHITE 0
#define BLACK 1
#define MAX 1000

void enQ(int arr[], int value, int *rear);
int deQ(int arr[], int *front);
int isValid(int x, int y, int N, int M);
int BFS(int arr[MAX][MAX],int cur_x,int cur_y, int N, int M,int cur_max, int color);

int main(void) {
  /*input*/
  int N, M;
  int graph[MAX][MAX];
  for(int i = 0; i< MAX ;i++){
    for(int j = 0; j< MAX; j++){
      graph[i][j] = 0;
    }
  }
  scanf("%d %d\n",&N,&M);
  for(int i = 0 ;i < N; i++){
    for(int j = 0; j < M; j++){
      scanf("%d ",&graph[i][j]);
    }
  }
  /*test
  printf("N:%d M:%d\n",N, M);
  printf("graph\n");
  for(int i =0 ;i <N; i++){
    for(int j =0; j < M; j++){
      printf("%d ",graph[i][j]);
    }
    printf("\n");
  }
  */

  int global_max = 0;
  for(int n = 0;n < N; n++){
    for(int m = 0; m < M ; m++){
      int cur_max = 0;
      if(graph[n][m] == BLACK){
        cur_max = BFS(graph, n, m, N, M, cur_max,BLACK);
      }
      else if(graph[n][m] == WHITE){
        cur_max = BFS(graph, n, m, N, M, cur_max,WHITE);
      }
      if(cur_max > global_max){
        global_max = cur_max;
      }
    }
  }
  
  printf("%d\n",global_max);

  return 0;
}

/*function section*/
void enQ(int arr[], int value,int *rear){
  arr[(*rear)++] = value;
  //printf("enQ:%d rear:%d\n",arr[(*rear)-1],*rear-1); 
}
int deQ(int arr[],int *front){
  //printf("deQ:%d front:%d\n",arr[*front],*front);
  return(arr[(*front)++]);
}

int isValid(int x, int y, int N, int M){
  if(x < 0 || x >= N || y < 0 || y >= M){//out of grid
    //printf("Invalid\n");
    return INVALID;
  }
  else{
    //printf("valid\n");
    return VALID;
  }  
}

int BFS(int arr[MAX][MAX],int cur_x,int cur_y, int N, int M, int cur_max,int color){
  /*
  printf("BFS\n");
  printf("graph\n");
  for(int i = 0;i < N;i++){
    for(int j = 0;j < M;j++){
      printf("%d ",arr[i][j]);
    }
    printf("\n");
  }*/
  
  int visited[N][M];
  for(int i = 0;i < N;i++){
    for(int j = 0;j < M;j++){
      visited[i][j] = UNVISITED;
    }
  }

  int Q[MAX];
  int front, rear;
  front = rear = 0;
  for(int i = 0 ;i < MAX;i++){
    Q[i] = 0;
  }

  enQ(Q, (cur_x*10) + cur_y, &rear);
  visited[cur_x][cur_y] = VISITED;
  
  int r[] = {1, -1, 0, 0};
  int c[] = {0, 0, 1, -1};

  //printf("cur_x:%d cur_y:%d\n",cur_x,cur_y);
  while(front != rear){//Q is empty
    //printf("Q is not empty\n");
    /*if(front > 5 || rear > 5){
      break;
    }
    */
    int tmp = 0;
    int tmp_x = 0;
    int tmp_y = 0;
    tmp = deQ(Q, &front);
    tmp_x = tmp / 10;
    tmp_y = tmp % 10;
    cur_max++;
    
    int x = 0;
    int y = 0;
    for(int i = 0; i < 4; i++){
      x = tmp_x + r[i];
      y = tmp_y + c[i];
      //printf("x:%d y:%d\n",x,y);
      if((isValid(x, y, N, M) == VALID) && visited[x][y] == UNVISITED &&(arr[x][y] == color)){
        enQ(Q, (10*x)+y, &rear);
        visited[x][y] = VISITED;
      }
    }

  }

  return cur_max;
}
