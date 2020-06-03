import React, { Component } from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import { Navbar, Nav, NavDropdown, FormControl, Form, Button } from 'react-bootstrap';
import axios from 'axios';
// const recipeScraper = require("recipe-scraper");
// import recipeScraper from 'recipe-scraper';

class Recipe extends Component {
	constructor(props) {
		super(props);
		this.value = "";
		this.state = {
			recipes: []
		};

		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}


	handleChange(event) {
		this.value = event.target.value;
		// console.log(this.value);
	}
	
	handleSubmit(event) {
		console.log(this.value);
		alert('A name was submitted: ' + this.value);
		axios.post('http://127.0.0.1:8000/api/recipe_url/', {url: this.value})
		.then(res => {
			console.log(res);
		});
		event.preventDefault();
	}
	
	async componentDidMount() {
		try {
			axios.get('http://127.0.0.1:8000/api/recipes/')
		  	.then(res => {
				const recipes = res.data;
				this.setState({recipes});
				console.log(recipes)
				console.log(this.state)
		  	})
		  // const res = await fetch('http://127.0.0.1:8000/api/recipe/'); // fetching the data from api, before the page loaded
		  // const recipes = await res.json();
		  // this.setState({
		  // 	recipes
		  // });
	  	} catch (e) {
			console.log(e);
	  	}
	}

	render() {
		return (
			<div>
				<br></br>
				<Form inline className="ml-3 block" >
					<FormControl type="text" placeholder="Enter URL" className="mr-sm-2" onChange={this.handleChange}/>
					<Button variant="primary" type="Submit" onClick={this.handleSubmit}>Scrape!</Button>
				</Form>
				<br></br>
				{this.state.recipes.map(item => (
				<div key={item.id}>
					<h1>{item.title}</h1>
					<span>{item.instructions}</span>
				</div>
        		))}
			</div>
		)
	}	
}

export default Recipe;