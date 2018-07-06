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
      this.setState({node: node}, scrollToHash);
    }).catch(e =>
      alert(e)
    );
  }

  render() {
    let node = this.state.node;
    return <div>
      <Router>        
        <Node node={node}/>
      </Router>
    </div>;
  }
}

const Node = ({node, l=0, traj="traj"}) => 
  <div className={"level" + l + " node"} 
       id={traj}
       style={{}}
       >
    <Link to={"#" + traj}><button>{node.v}</button></Link>
    
    <pre>{node.t.join("")}</pre>
    {node.c.map((c, i) => <Node node={c} l={l+1} traj={traj + i}/>)}
  </div>


