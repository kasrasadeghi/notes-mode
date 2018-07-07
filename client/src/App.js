import React, { Component } from 'react';


// const pprint = (s) => JSON.stringify(s, null, 2);
const str = (s) => JSON.stringify(s);

const scrollToHash = () => {
  let path = decodeURI(window.location.href.split(window.location.origin)[1]);
  let id = (path)? '/' + path.split('#')[1] : "";
  if (id && document.getElementById(id)) {
    document.getElementById(id).scrollIntoView();
  }
}

const fold = (node) => {
  let l = [];
  l.push(node);
  for (let c of node.c) {
    l = l.concat(fold(c));
  }
  return l
}

export default class App extends Component {
  constructor() {
    super();
    this.state = {
      root: {v: 'Loading...', 'c': [], 't': []}
    }

    this.getRoot(window.location.hostname, (e) => this.getRoot('localhost:5000'));
  }

  getRoot(hostname, failure=(e) => alert(e)) {
    fetch(' http://' + hostname + '/current', {
      method: 'GET',
      dataType: 'json'
    })
    .then(r => r.json())
    .then(root => {
      if ('error' in root) {
        throw root['error'];
      }
      this.setState({root}, scrollToHash);
    } 
    ).catch(e =>
      failure(e)
    );
  }

  enter(path) {
    window.history.pushState({path}, "", window.location.origin + "/" + path);
    this.setState({}, scrollToHash);
  }

  componentDidMount() {
    window.addEventListener('popstate', (e) => {
      //TODO do something with history?
      this.setState({}, scrollToHash);
    });
  }

  pathToNode(path, root=this.state.root) {
    return fold(root).filter(n => n.path === path)[0];
  }

  render() {
    let path = decodeURI(window.location.href.split(window.location.origin)[1]);
    path = (path)? path.split('#')[0] : "";
    if (this.state.root.v === 'Loading...') {
      return <div>
          <pre>path: {path}</pre>
          <pre>root value: {this.state.root.v}</pre>
          <button className='c' style={{color: 'rgb(230, 230, 230)'}}>Loading...</button>
        </div>;
    }

    let current = this.pathToNode(path);

    if (current) {
      return <div>
        <pre>path: {path}</pre>
        <pre>root value: {this.state.root.v}</pre>
        <Node node={current}
              path={path} 
              enter={(currentPath) => this.enter(currentPath)}
        />
      </div>;
    } else {
      return <pre>
          fix your path: {path}
        </pre>;
    }
  }
}


const Node = ({node, enter}) => 
  <div className={"c" + node.l + " node"} id={node.path} >
    <button onClick={() => {
      window.history.pushState({}, "", "#" + node.path.slice(1));
      scrollToHash();
    }} className={"c c" + node.l}>{node.v}</button>
    <button onClick={() => enter(node.path.slice(1))} className={"l l" + node.l}>enter</button>
    
    <pre>{node.t.join("")}</pre>
    {node.c.map((c) => 
      <Node node={c}
            enter={enter}
      />)}
  </div>


