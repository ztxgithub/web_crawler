# python 网络爬虫
 
## pyhton 技术选型

```shell

    1.requests 和 beautifulsoup 都是库， scrapy是框架(在这个框架中可以应用requests 和 beautifulsoup库)
    2.scrapy基于twisted，性能是最大的优势，这是异步IO的框架
    3.scrapy方便扩展，提供很多的内置的功能
    4.scrapy内置css和xpath selector非常方便，beautifulsoup最大的缺点就是慢

```

## 网页的分类

```shell
    1.静态网页
        事先在服务器端生成好的页面，这个页面的内容是不会变的，浏览器在请求的时候抓取就行了。常见的CSS就是静态页面
    2.动态网页
        请求某一商品页面是根据我们传递的参数不同，通过服务器从数据库中取出数据然后返回给浏览器。像淘宝
    3.webservice(restapi)
        它实际是动态网页的一种，只是通过ajax方式和后台restapi来进行交互，
```

## 爬虫的作用

```shell
    1.搜索引擎(google)
        垂直领域的搜索引擎，只在相关领域进行搜索
        
    2.推荐引擎
        例如今日头条，推送感兴趣的内容，每天去爬取大量的网站，将这些数据进行分析，它与搜索引擎不同，搜索引擎是我们人为主动
        去搜索，而推荐引擎是根据我们的浏览习惯，进行数据分析并推送
        
    3.机器学习的数据样本
        
    4.数据分析(金融数据分析)，舆情分析
```

## 网站url的结构图

```shell
    1.一个网站是分层设计的，例如伯乐在线的顶级域名 http://www.jobbole.com/，其下面的文章子域名(二级域名)
       http://blog.jobbole.com/，那么具体什么文章则是http://blog.jobbole.com/123
    2.爬虫时要考虑到网站中url会有环路，比如url1对应一个网页1，在网页1中有url2，在url2中的网站又指向了url1，可以通过
      去重(生成url列表，对爬过的url加入到该列表中，下次要对下一个url进行爬虫时在列表中考虑是否已经爬过了)
```

## 深度优先算法(利用递归)

```shell
    def depth_tree(tree_node):
        if tree_node is not None:
            print(tree_node._data)
            if tree_node._left if not None:
                return depth_tree(tree_node._left)
            if tree_node._right if not None:
                return depth_tree(tree_node._right)
```
## 广度优先算法(利用队列)

```shell
    def level_queue(root):
        if root is None:
            return
        my_queue = []
        node = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop()
            print(node.elem)
            if node.lchild is not None:
                my_queue.append(node.lchild)
            if node.rchild is not None:
                my_queue.append(node.rchild)
```

## 爬虫去重策略

```shell
    方法一:
        将访问过的url保存到数据库中，当我们获取下一个url的时候，就从数据库中查询url是否被获取过了，缺点是效率非常低
    方法二:
        将访问过的url保存到set中，只需要o(1)的代价就可以查询到url
        缺点是内存越来越大，有1亿条url，内存占用了 100000000*2byte*50字符/1024/1024/1024 = 9GB
    方法三:
        url经过md5等方法进行哈希后(将字符缩减到固定长度)保存到set中 
        缺点存在hash冲突
    方法四:(不太适用)
        用bitmap方法，将访问过的url通过hash函数映射到某一位
        缺点也是hash冲突非常高
    方法五:(推荐使用)
        bloomfilter方法对bitmap进行改进，多重hash函数降低冲突
```