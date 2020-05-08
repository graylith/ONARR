import React,{Component} from 'react';
import {Pie} from 'react-chartjs-2';
class CategoryRatio extends Component{
    data= {
            labels:this.props.category,
            datasets: [
                {                  
                    data: this.props.value,
                    backgroundColor:['#EC407A','#E3F2FD','#F06292','#CDDC39','#EA80FC','#FF8A65','#81C784',
                                    '#64B5F6','#CE93D8','#33691E','#D4E157','##66BB6A','#9CCC65','#FF7043',
                                    '#69F0AE','#1A237E','#8C9EFF'],
                    borderWidth:0.5,
                    borderColor:'white',
                    hoverBorderWidth:1,
                    hoverBorderColor:'white'
                }
     ]
    }
    render(){

    return (
        <div>
            <Pie data={this.data} onElementsClick={this.onCategoryClick}   
                width={100}
                height={80} 
                onElementsClick={elems => {
                    localStorage.setItem('keyword',elems[0]._model.label);
                    window.location = "/category"
                }}
            />
        </div>
    ) 
   }
}
export default CategoryRatio;



