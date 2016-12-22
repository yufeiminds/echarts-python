# Echarts Python Sample

A simple flask server && A simple html with webpack

## Code

### Python

```python
@app.route('/opt/bar')
def bar():
    chart = Echart('GDP', 'This is a fake chart')
    chart.use(Bar('China', [2, 3, 4, 5]))
    chart.use(Legend(['GDP']))
    chart.use(Axis('category', 'bottom', data=['Nov', 'Dec', 'Jan', 'Feb']))
    return jsonify(chart.json)
```

### ES5

```javascript
// XHR callback
function callback () {
  var chart = echarts.init(document.getElementById('main'));
  chart.setOption(response.data)
}
```

### ES6

```javascript
fetch('http://127.0.0.1:5000/opt/bar').then(resp => {
  var chart = echarts.init(document.getElementById('main'));
  chart.setOption(response.data)
})
```

## Run Example

### Server

```
pip install -r requirements.txt

python -m index
```

### Frontend

```
sudo npm install

webpack
```

### Open Page

```
python -m SimpleHTTPServer

open http://localhost:8000/
```
