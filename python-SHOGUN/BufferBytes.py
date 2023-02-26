#!/usr/bin/python3
# encoding: utf-8
class BufferBytes_(object):
    """
        The byte-buffered queue, suitable for multithreaded operations and use, is a basic buffered queue
        His basic functions are divided into: queue,push, pop, query, persist, get, persist_put, BufferSpace,
        GetBufferSpace, QueryBufferSpace, detailed features, see details
        author：ios_shogun-Atomic君
        date:2023-2-24
        self:IOS_SHOGUN_studio
    """

    def __init__(self, **data: bytes | int | None) -> None:
        """
            Create a blocking byte buffer, you can give him the initial item,
            you can also define its size, which defaults to infinity
            [创建一个阻塞字节缓冲区，你可以给他初始项目，你也可以定义它的大小，默认为无穷大]
        """

    pass

    def queue(self, ts: int, **data: bytes | None) -> None:
        """
            Cache queue, tuple storage, you can set his response time in milliseconds
            Of course you can set this as None, which is the default
            [缓存队列，元组存储，可以设置他的响应时间以毫秒为单位 当然你可以把它设置为 None，这是默认的]
        """

    pass

    def push(self, **data: bytes, ) -> None:
        """
            Push into the cache queue, just divided into it, in the form of a dictionary
            [以字典的形式推送到缓存队列中，只是划分为缓存队列]
        """

    pass

    def pop(self) -> bytes | None:
        """
            The first data of the buffer is removed from the header and the data is returned
            [缓冲区的第一个数据从标头中删除并返回数据]
        """

    pass

    def query(self) -> str:
        """
            The status of the query buffer, generally divided into, is empty or full |
            with a persistent license
            [查询缓冲区的状态（通常分为）为空或已满 |使用永久许可证]
        """

    pass

    def persist(self, path: str) -> bool:
        """
            To persist all buffer data, you need to provide all the storage methods
            [若要持久保存所有缓冲区数据，需要提供所有存储方法]
        """

    pass

    def get(self, index: int | str) -> bytes | None:
        """
            More dictionaries or indexes fetch objects into buffers
            [更多字典或索引将对象提取到缓冲区中]
        """

    pass

    def persist_put(self, index: int | str, path: str) -> bool:
        """
            Persist individual buffer objects based on dictionaries or indexes
            [基于字典或索引保留单个缓冲区对象]
        """

    pass

    def BufferSpace(self, index: int) -> None:
        """
            Manually changing the buffer space at a later stage cannot be smaller
            than the current space
            [在稍后阶段手动更改缓冲区空间不能小于当前空间]
        """

    pass

    def GetBufferSpace(self) -> int:
        """
            Gets the space used by the current buffer
            [获取当前缓冲区使用的空间]
        """

    pass

    def QueryBufferSpace(self) -> int | None:
        """
            Query the remaining buffer space, expressed as the maximum space used in infinite mode
            [查询剩余缓冲区空间，表示为无限模式下使用的最大空间]
        """

    pass

    def clearBuffered(self) -> None:
        """
            Empty all queues for the buffer
            [清空缓冲区的所有队列]
        """

    pass

    def clearIndex(self) -> None:
        """
            Empty all index for the buffer
            [清空缓冲区的所有索引]
        """

    pass

    def ExportData(self) -> list[bytes] | None:
        """
            Export all bytes of data
            [导出全部的字节数据]
        """

    pass

    def ClearExportData(self) -> list[bytes] | None:
        """
            Export all bytes of data and clear all data
            [导出全部的字节数据并且清除全部的数据]
        """

    pass

    def ReentrancyMode(self, mode: int, accessibility: int = -1) -> None:
        """
            [切换缓冲区的模式-可参考:BOUNDLESS|LIMITED]
        """
    pass

    def __Del(self, target: dict | list, key: str) -> None:
        """
            :param target: target dict
            :param key: index key
            :return: None
            The intrinsic function is mainly used as a delete
            [内部函数主要作为删除作用]
        """
    pass

    def opencv(self):
        """
        Gets a view object that summarizes the buffer
        :return:获取一个概括缓冲区的一个视图对象
        """
        return self.__repr__()
    pass


pass
