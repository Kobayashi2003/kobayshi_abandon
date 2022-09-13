# 内联和嵌套命名空间

内联命名空间能够把空间内函数和类型导出到父命名空间中，这样即使不指定子命名空间也可以使用其空间中的类型和函数

```cpp
// C++ 11
namespace A {
    inline namespace B {
        ...
    }
}
```

**嵌套命名空间的简化语法**

```cpp
// C++ 17
namespace A::B::C {
    int foo() {return 17}
}

// C++ 20
namespace A::B::inline C {
    int foo() {return 20}
}
```
