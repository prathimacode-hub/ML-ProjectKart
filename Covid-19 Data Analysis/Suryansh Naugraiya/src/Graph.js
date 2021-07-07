import React, { PureComponent } from 'react';
import DonutChart from "react-svg-donut-chart";

class Graph extends PureComponent {
    constructor(props) {
        super(props)
        this.state = {

        }
    }

    render() {
        const data = [
            { value: 30, stroke: "rgb(160, 39, 39)" },
            { value: 20, stroke: "rgb(53, 158, 40)" },
            { value: 50, stroke: "rgb(28, 115, 255)" }
        ]
        return (
            <div className="graph">
                <DonutChart data={data}></DonutChart>
                <div className="graph-items">
                    <div class="graph-deaths graph-item"><div></div>Deaths</div>
                    <div class="graph-recovered graph-item"><div></div>Recovered</div>
                    <div class="graph-active graph-item"><div></div>Active</div>
                </div>
            </div>
        )
    }
}

export default Graph;