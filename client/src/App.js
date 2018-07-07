import React, { Component } from 'react';


// const pprint = (s) => JSON.stringify(s, null, 2);
const str = (s) => JSON.stringify(s);

const scrollToHash = () => {
  const hash = window.location.hash;
  const id = (hash) ? hash.slice(1) : '';
  if (id && document.getElementById(id)) {
    document.getElementById(id).scrollIntoView();
  }
}

export default class App extends Component {
  constructor() {
    super();
    this.state = {
      root: {v: 'Loading...', 'c': [], 't': []},
      current: undefined,
      currentPath: undefined,
      history: []
    }

    this.getRoot(window.location.hostname, (e) => this.getRoot('localhost:5000'));
  }

  getRoot(hostname, failure=(e) => alert(e)) {
    fetch(' http://' + hostname + '/current', {
      method: 'GET',
      dataType: 'json'
    })
    .then(r => r.json())
    .then(node => {
      if ('error' in node) {
        throw node['error'];
      }
      this.setState({root: node, current: node, currentPath: node.v}, scrollToHash)
    } 
    ).catch(e =>
      failure(e)
    );
  }

  enter(current, currentPath) {
    window.history.pushState({current: this.state.current, currentPath: this.state.currentPath}, "", window.location.origin + "/" + currentPath);
    let history = this.state.history;
    history.push({current, currentPath});
    this.setState({current, currentPath});
  }

  componentDidMount() {
    window.addEventListener('popstate', (e) => {
      let history = this.state.history;
      history.pop();
      // let {current, currentPath} = history.pop();
      // if (e.state) {
        // current = e.state.current; 
        // currentPath = e.state.currentPath;
      // }
      let currentPath = window.location.pathname.slice(1);
      let current = this.pathToNode(currentPath);
      console.log('popping path to: ', currentPath);
      this.setState({current, currentPath, history});
    });
  }

  pathToNode(path, root=this.state.root) {
    console.log(path +", "+ root.v + " => ");
    let rest = path.slice(root.v.length);
    console.log(rest);
    if (rest === "") {
      console.log('  node:', root.v)
      return root;
    }
    for (let c in root.c) {
      if (rest.startsWith(c.v)) {
        return this.pathToNode(rest, c);
      }
    }
  }

  render() {
    let current = this.state.current || this.state.root;
    let path = window.location.pathname.slice(1);
    return <div>
      <pre>path: {path}</pre>
      <pre>root value: {this.state.root.v}</pre>
      <pre>current value: {(this.state.current)? this.state.current.v : ""}</pre>
      <pre>current path:  {this.state.currentPath}</pre>
      <pre>{str(this.state)}</pre>
      <pre>{str(this.pathToNode(path, current))}</pre>
      <Node node={current}
            path={path} 
            enter={(current, currentPath) => this.enter(current, currentPath)}
      />  
      
      </div>
    ;
  }
}


const Node = ({node, l=0, path=node.v, enter}) => 
  <div className={"c" + l + " node"} id={path} >
    <button onClick={() => {
      window.history.pushState({}, "", "#" + path);
      scrollToHash();
    }} className={"c c" + l}>{node.v}</button>
    <button onClick={() => enter(node, path)} className={"l l" + l}>enter</button>
    
    <pre>{node.t.join("")}</pre>
    {node.c.map((c) => 
      <Node node={c} 
            l={l+1} 
            path={path.endsWith('/') ? path + c.v : path + '/' + c.v}
            enter={enter}
      />)}
  </div>


