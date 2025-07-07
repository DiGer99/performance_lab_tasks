### Переход в рабочую директорию
```shell
  cd performance_lab_tasks
```
### Установка прав на рабочую директорию
ПКМ performance_lab_tasks -> Mark Directory as -> Sources root

### Установка зависимостей

Если нет uv
```shell
  pip install uv
```

Синхронизация с uv.lock
```shell
  uv sync
```
### Установка виртуального окружения в директории uv

```shell
  source .venv/bin/activate
```

# Запуск
## task1
```shell
  python3 -m task1.task1 5 4
```

## task2
```shell
  python3 -m task2.task2 "task2/circle.txt" "task2/dot.txt"
```

## task3
```shell
  python3 -m task3.task3 "task3/values.json" "task3/tests.json" "task3/report.json"
```

## task4 
```shell
  python3 -m task4.task4 "task4/nums.txt"
```