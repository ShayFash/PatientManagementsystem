import React from 'react';
import { Link } from 'react-router-dom';

class NewNote extends React.Component {
    constructor(props) {
        super();
        this.state={
            noteText: "",
            diagnosisText: ""
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        const {name, value} = event.target;
        this.setState({[name]: value})
    }

    render() {
        return (
            <div>
                <form className="homeContainer" style={{padding: "50px"}}>
                    <span style={{marginRight: "700px", fontSize: "24px", fontWeight: "bold", fontStyle: "italic"}}>New Note:</span>
                    <Link to="/">
                        <button className="navBarButton">Back</button>
                    </Link>
                    <br/>
                    <textarea
                    placeholder="Insert Text"
                    name="noteText" 
                    value={this.state.noteText}
                    onChange={this.handleChange}
                    style={{width:"900px", height: "450px", fontSize: "24px"}}
                    >
                    </textarea>
                    <br />
                    <input
                    type="text" 
                    placeholder="Diagnosis"
                    name="diagnosisText"
                    value={this.state.diagnosisText}
                    onChange={this.handleChange}
                    style={{width:"450px", fontSize: "16px", marginRight: "450px"}}
                    >
                    </input>
                    <br/>
                    <Link to="/">
                        <button style={{marginRight: "850px", marginTop: "20px"}} className="navBarButton">Post</button>
                    </Link>
                    
                </form>
            </div>
        )
    }
}

export default NewNote;