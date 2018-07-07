import React, { Component } from 'react';

import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom';
import { HashLink as Link } from 'react-router-hash-link';

let scrollToHash = () => {
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
      currentPath: undefined
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
      this.setState({node: node, current: node, currentPath: node.v}, scrollToHash)
    } 
    ).catch(e =>
      failure(e)
    );
  }

  enter(current, currentPath) {
    this.setState({current, currentPath});
  }

  pathToNode(path, root=this.state.root) {
    console.log(path, root)
    let rest = path.slice(root.v.length);
    console.log(rest);
    if (rest === "") {
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
    return <div>
      <Router>
        <Route exact path="/:path" render={({match}) => 
          <div>
          <pre>{JSON.stringify(match)}</pre>
          <pre>{JSON.stringify(window.location.path)}</pre>
          </div>
          // <Node node={this.pathToNode(match.params.path)} 
          //       path={match.params.path} 
          //       enter={(current, currentPath) => this.enter(current, currentPath)}
          // />
        }/>
      </Router>
    </div>;
  }
}


const Node = ({node, l=0, path=node.v, enter}) => 
  <div className={"c" + l + " node"} id={path} >
    <Link to={"#" + path}><button className={"c c" + l}>{node.v}</button></Link>
    <Link to={path}><button onClick={() => enter(node, path)} className={"l l" + l}>enter</button></Link>
    
    <pre>{node.t.join("")}</pre>
    {node.c.map((c) => 
      <Node node={c} 
            l={l+1} 
            path={path.endsWith('/') ? path + c.v : path + '/' + c.v}
            enter={enter}
      />)}
  </div>


