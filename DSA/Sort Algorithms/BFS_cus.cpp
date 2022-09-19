#include <stdio.h>
#define VISITED 1
#define UNVISITED 0
#define VALID 1
#define INVALID 0
#define WHITE 0
#define BLACK 1
#define MAX 1000

int graph[MAX][MAX];

void enQ(int arr[], int value, int rear);
int deQ(int arr[], int front);
int isValid(int x, int y, int N, int M);
int BFS(int *arr[],int cur_x,int cur_y, int N, int M,int cur_max);

int main(void) {
  /*input*/
  int N, M;
  scanf("%d %d\n",&N,&M);
  for(int i = 0; i< MAX ;i++){
    for(int j = 0; j< MAX; j++){
      graph[i][j] = 0;
    }
  }
  for(int i = 0 ;i < N; i++){
    for(int j = 0; j < M; j++){
      scanf("%d",&graph[i][j]);
    }
  }
  int global_max = 0;
  for(int n = 0;n < N; n++){
    for(int m = 0; m < M ; m++){
      int cur_max = 0;
      if(graph[n][m] == BLACK){
        continue;
      }
      else{//BFS
        BFS(graph, n, m, N, M, cur_max);
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
void enQ(int arr[], int value,int rear){
  arr[rear++] = value; 
}
int deQ(int arr[],int front){
  return(arr[front]++);
}

int isValid(int x, int y, int N, int M){
  if(x < 0 || x > N || y < 0 || y > M){//out of grid
    return INVALID;
  }
  else{
    return VALID;
  }  
}

int BFS(int *graph[],int cur_x,int cur_y, int N, int M, int cur_max){

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

  enQ(Q, graph[cur_x][cur_y], rear);
  
  int r[] = {1, -1, 0, 0};
  int c[] = {0, 0, 1, -1};
  
  while((front != rear) && (front != 0)){//Q is empty
    
    deQ(Q, front);
    visited[cur_x][cur_y] = VISITED;
    cur_max++;
    for(int i = 0; i < 4; i++){
      cur_x += r[i];
      cur_y += c[i];
      if((isValid(cur_x, cur_y, N, M) == VALID) && visited[cur_x][cur_y] == UNVISITED &&(graph[cur_x][cur_y] == WHITE)){
        enQ(Q, graph[cur_x][cur_y], rear);
      }
    }

  }

  return cur_max;
}
