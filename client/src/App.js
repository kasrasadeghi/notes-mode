import React, { Component } from 'react';
import './App.css';

const scrollOptions = {block: 'start'}

window.onpopstate = e => {
  // https://stackoverflow.com/questions/824349/modify-the-url-without-reloading-the-page
  // if (e.state) {
    let {scroll} = e.state;
    console.log(e.state);
    
    document.getElementById(scroll).scrollIntoView(scrollOptions);
  // }
}

export default class App extends Component {
  constructor() {
    super();
    this.state = {
      node: {v: 'Loading...', 'c': [], 't': []}
    }

    fetch(' http://' + window.location.hostname + '/current', {
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

const Node = ({node, l=0, traj="traj"}) => 
  <div className={"level" + l + " node"} 
       id={traj}
       style={{display: 'block', 'margin-left': '2%', 'margin-right': '0.5%'}}
       >
    <button onClick={() => {
              let current = 
                  (window.location.href.endsWith('/')) ? 'traj' :
                  window.location.href.split('#').slice(-1).pop();
              
              window.history.pushState({scroll: current}, undefined, "/#" + traj);
              console.log('pushing', {scroll: current});
              document.getElementById(traj).scrollIntoView(scrollOptions);
            }}>
      {node.v}
    </button>
    <pre>{node.t.join("")}</pre>
    {node.c.map((c, i) => <Node node={c} l={l+1} traj={traj + i}/>)}
  </div>


