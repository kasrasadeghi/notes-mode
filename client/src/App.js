import React, { Component } from 'react';
import './App.css';

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
      node: {v: 'Loading...', 'c': [], 't': []}
    }

    fetch(' http://' + window.location.hostname + '/current', {
    // fetch(' http://localhost:5000/current', {
      method: 'GET',
      dataType: 'json'
    })
    .then(r => r.json())
    .then(node => {
      if ('error' in node) {
        throw node['error'];
      }
      this.setState({node: node}, scrollToHash)
    } 
    ).catch(e =>
      alert(e)
    );
  }

  render() {
    return <div>
      <Router>
        <Node node={this.state.node} path={this.state.node.v}/>
      </Router>
    </div>;
  }
}

const Node = ({node, l=0, path=node.v}) => 
  <div className={"level" + l + " node"} 
       id={path}
       style={{}}
       >
    <Link to={"#" + path}><button className={"level" + l}>{node.v}</button></Link>
    
    <pre>{node.t.join("")}</pre>
    {node.c.map((c) => <Node node={c} l={l+1} path={
      path.endsWith('/') ? path + c.v : path + '/' + c.v
    }/>)}
  </div>


