// 导入axios实例
import service from '@/request/index'
import Qs from 'qs'

// 定义接口的传参
interface ITime_Return {
    Date_start: string;
    Date_end: string;
}

export function apiSendTime(param: ITime_Return) {
    return service({
        url: 'post/',
        method: 'post',
        data: param
    })
}