## Python 实现设计模式
hehe
#### 目录

- 创建型模式

    抽象了实例化过程

    - 抽象工厂(ABSTRACT_FACTORY)

        提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。

        [example](examples/abstract_factory.py)

    - 生成器(BUILDER)

        将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

        [example](examples/builder.py)


    - 工厂方法(FACTORY_METHOD)

        定义一个用于创建对象的接口，让子类决定实例化哪一个类。 Factory Method使一个类的实例化延迟到其子类。

        [example](examples/factory_method.py)

    - 原型(PROTOTYPE)

         原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。

        [example](examples/prototype.py)

    - 单件(SINGLETON)

         保证一个类仅有一个实 ，并提供一个访问它的全局访问点。

        [example](examples/singleton.py)

- 结构性模式

    结构型模式涉及如何组合类和对象以获得更大的结构

    - 适配器(ADAPTER)

        将一个类的接口转换成客户希望的另外一个接 。 Adapter模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

        [example](examples/adapter.py)

    - 桥接(BRIDGE)

    - 组合(COMPOSIBLE)

    - 装饰(DECORATOR)

        动态地给一个对象添加一些额外的职责。就增加功能来说， Decorator模式相比于成子类更为为灵活。

        [example](examples/decorator.py)

    - 外观(FACEDE)

        为子系统中的一组接口提供一个一致的界面， Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

        [example](examples/facede.py)

    - 享元(FLYWEIGHT)

        运用共享技术有效的支持大量细粒度的对象。

        [example](examples/flyweight.py)

    - 代理(PROXY)

        为其他对象提供一种代理以控制这个对象的访问。

        [example](examples/proxy.py)

- 行为模式

    行为模式涉及到算法和对象间职责的分配

    - 职责链(CHAIN_OF_RESPONSIBILITY)

        使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

        [example](examples/chain_of_responsibility.py)

    - 命令(COMMAND)

        将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化;对请求排队或记录请求日志，以及支持可撤消的操作。

        [example](examples/command.py)

    - 解释器(INTERPRETER)

        给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。

        [example](examples/interpreter.py)

    - 迭代器(ITERATOR)

    - 中介者(MEDIATOR)

    - 备忘录(MEMENTO)

    - 观察者(OBSERVER)

        定义对象间的一种一对多的依赖关系 ,当一个对象的状态发生改变时 , 所有依赖于它的对象都得到通知并被自动刷新。

        [example](examples/observer.py)

    - 状态(STATE)

        允许一个对象在其内部状态改变时改变它的行为。对象看起来似乎修改了它的类。

        [example](examples/state.py)

    - 策略(STRATEGY)

        定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化。

        [example](examples/strategy.py)

    - 模版方法(TEMPLATE_METHOD)

        定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。 TemplateMethod使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

        [example](examples/template_method.py)

    - 访问者(VISITOR)


