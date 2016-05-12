/*
  Initilizing echarts samples.
*/

import Echart from 'echarts'

var chart = Echart.init(document.getElementById('main'))
chart.showLoading()

var ht = {}

var sendXHR = (request) => {

  var { method, url, data, headers } = request

  var xhr = new XMLHttpRequest(), response = { url: url }, handler
  xhr.open(request.method, url, true)

  handler = (event) => {

    response.data = JSON.parse(xhr.responseText)
    response.status = xhr.status
    response.statusText = xhr.statusText
    response.headers = xhr.getAllResponseHeaders()

    chart.setOption(response.data)
    console.log('Response > ', response)
    chart.hideLoading()

  }

  xhr.timeout = 0
  xhr.onload = handler
  xhr.onabort = handler
  xhr.onerror = handler
  xhr.ontimeout = function () {}
  xhr.onprogress = function () {}

  for (header in request.headers || {})
    xhr.setRequestHeader(header, request.headers[header])

  xhr.send(request.data);
}

ht.loadChart = (url, data = {}, headers = {}) => {
  var request = {
    method: 'get',
    url: url,
    data: data,
    headers: headers
  }
  return sendXHR(request)
}

ht.loadChart('http://127.0.0.1:5000/opt/bar')
