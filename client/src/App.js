import React, { Component } from 'react';
import './App.css';


export default class App extends Component {
  constructor() {
    super();
    this.state = {
      node: {v: 'Loading...', 'c': [], 't': []}
    }

    fetch('http://f29ad0e1.ngrok.io/current', {
      method: 'GET',
      dataType: 'json'
    })
    .then(r => r.json())
    .then(node => 
      this.setState({node: node})
    ).catch(e =>
      alert(e)
    );
  }

  render() {
    let node = this.state.node;
    return <div>
      <Node node={node}/>
    </div>;
  }
}

const Node = ({node, l=0}) => 
  <div className={"level" + l} 
       style={{display: 'block', 'margin-left': '2%', 'margin-right': '0.5%'}}
       >
    <b>{node.v}</b>
    <pre>{node.t.join("")}</pre>
    {node.c.map(c => <Node node={c} l={l+1}/>)}
  </div>


