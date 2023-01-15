// 导入axios实例
import service from '@/request/index'

// 定义接口的传参
interface IResult_URL {
    Image_URL: string;
    Feature_URL: string;
}

interface ITime_Return {
    Date_start: string;
    Date_end: string;
}

// 获取URL信息
// export function apiGetURL(param: ITime_Return) {
//     return service({
//         url: '/categorys',
//         method: 'get',
//         data: param
//     })
// }


export function apiGetURL() {
    return service({
        url: 'post/',
        method: 'get',
    })
}


// export function apiGetURL(param: ITime_Return) {
//     return service({
//         url: 'post/',
//         method: 'get',
//         params: param
//     })
// }