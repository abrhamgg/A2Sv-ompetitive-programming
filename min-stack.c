#define MAX 1000

typedef struct {
    int s[MAX];
    int top;
} MinStack;


MinStack* minStackCreate() {
    MinStack* s = (MinStack*) malloc(sizeof(MinStack));
    s->top = -1;
    return s;
}

void minStackPush(MinStack* obj, int val) {
  if (obj->top != MAX - 1) {
      obj->top++;
      obj->s[obj->top] = val;
  }
}

void minStackPop(MinStack* obj) {
  if (obj->top != -1) {
      obj->top--;
  }
}

int minStackTop(MinStack* obj) {
  return obj->s[obj->top];
}

int minStackGetMin(MinStack* obj) {
  int min = obj->s[0];
  for (int i = 0; i <= obj->top; i++) {
      if (obj->s[i] < min)
        min = obj->s[i];
  }
  return min;
}

void minStackFree(MinStack* obj) {
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/
