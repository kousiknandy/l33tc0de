#include <stdlib.h>
#include <stdio.h>

struct cache_entry {
  struct cache_entry *prev;
  struct cache_entry *next;
  int value;
  int key;
};

struct key {
  struct cache_entry *value;
  struct key *next;
  int key;
};

#define HASHTABLESZ 64 

int _hash (int key)
{
  return key % HASHTABLESZ;
}

typedef struct {
  struct key *hashtable[HASHTABLESZ];
  struct cache_entry *head;
  struct cache_entry *tail;
  int capacity;
  int current;
} LRUCache;

LRUCache* lRUCacheCreate(int capacity) {
  int i;
  LRUCache *this = malloc(sizeof *this);
  if (!this) return this;
  for (i=0; i<HASHTABLESZ; i++) this->hashtable[i] = NULL;
  this->head = NULL;
  this->tail = NULL;
  this->capacity = capacity;
  this->current = 0;
  return this;
}

void _prepend(LRUCache *obj, struct cache_entry *entry) {
  printf("_prepend %p\n", entry);
  if (obj->head == entry) return;
  if (entry->prev) entry->prev->next = entry->next;
  if (entry->next) entry->next->prev = entry->prev;
  if (!obj->tail) obj->tail = entry;
  else if (obj->tail == entry) obj->tail = entry->prev;
  if (obj->head) obj->head->prev = entry;
  entry->next = obj->head;
  entry->prev = NULL;
  obj->head = entry;
  printf("head-> %p tail-> %p\n", obj->head, obj->tail);
  printf("head->next %p tail->prev %p\n", obj->head->next, obj->tail->prev);
}

void _delete(LRUCache *obj, struct cache_entry *entry) {
  printf("_delete %p\n", entry);
  if (obj->head == entry) obj->head = entry->next;
  if (obj->tail == entry) obj->tail = entry->prev;
  if (entry->prev) entry->prev->next = entry->next;
  if (entry->next) entry->next->prev = entry->prev;
}

void _evict_lru(LRUCache *obj) {
   printf("_evict %d\n", obj->tail->key);
  if (obj->tail) _delete(obj, obj->tail);
}

struct cache_entry *_locate(LRUCache *obj, int key) {
  struct key *keylist = obj->hashtable[_hash(key)];
  printf("_locate %d\n", key);
  if (!keylist) return NULL;
  while (keylist) {
    if (keylist->key == key) return keylist->value;
    keylist = keylist->next;
  }
  return NULL;
}

void _makekey(LRUCache *obj, int key, struct cache_entry *value) {
  printf("_makekey %d %p\n", key, value);
  struct key *kp = malloc(sizeof *kp);
  kp->value = value;
  kp->key = key;
  kp->next = obj->hashtable[_hash(key)];
  obj->hashtable[_hash(key)] = kp;
}

void _rmkey(LRUCache *obj, int key) {
  printf("_rmkey %d\n", key);
  struct key *kp = obj->hashtable[_hash(key)];
  struct key *prev = kp;
  while (kp) {
    if (kp->key == key) {
      if (kp != prev) {
	prev->next = kp->next;
      } else {
	obj->hashtable[_hash(key)] = kp->next;
      }
      free(kp);
    }
    kp = kp->next;
    if (kp != prev) prev = prev->next;
  }
}

int lRUCacheGet(LRUCache* obj, int key) {
  struct cache_entry *entry = _locate(obj, key);
  if (entry) {
    _prepend(obj, entry);
    return entry->value;
  }
  return -1;
}

void lRUCachePut(LRUCache* obj, int key, int value) {
  struct cache_entry *entry = _locate(obj, key);
  if (entry) {
    _prepend(obj, entry);
    entry->value = value;
    return;
  }
  if (obj->current < obj->capacity) {
    struct cache_entry *entry = malloc(sizeof *entry);
    entry->value = value;
    entry->key = key;
    entry->prev = NULL;
    entry->next = NULL;
    _prepend(obj, entry);
    _makekey(obj, key, entry);
    obj->current++;
    return;
  }
  struct cache_entry *toevict = obj->tail;
  _evict_lru(obj);
  _rmkey(obj, toevict->key);
  toevict->value = value;
  toevict->key = key;
  _prepend(obj, toevict);
  _makekey(obj, key, toevict);
}

void lRUCacheFree(LRUCache* obj) {
    
}

/**
 * Your LRUCache struct will be instantiated and called as such:
 * struct LRUCache* obj = lRUCacheCreate(capacity);
 * int param_1 = lRUCacheGet(obj, key);
 * lRUCachePut(obj, key, value);
 * lRUCacheFree(obj);
 */

int main(int ac, char **av) {
   LRUCache* obj = lRUCacheCreate(2);
   int v = lRUCacheGet(obj, 10);
   printf("%d\n", v);
   lRUCachePut(obj, 2, 1);
   lRUCachePut(obj, 3, 2);
   v = lRUCacheGet(obj, 3);
   printf("%d\n", v);
   v = lRUCacheGet(obj, 2);
   printf("%d\n", v);
   lRUCachePut(obj, 4, 3);
   v = lRUCacheGet(obj, 2);
   printf("%d\n", v);
   v = lRUCacheGet(obj, 3);
   printf("%d\n", v);
   v = lRUCacheGet(obj, 4);
   printf("%d\n", v);
   return 0;
}
