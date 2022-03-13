class a extends React.Component {
    constructor(props)
    {
      super(props);
       this.state = {
         date : new Date(),
         clickedStatus: false,
         list:[]
       };
    }
    componentWillMount() {
        console.log('Component will mount!')
     }
    componentDidMount() {
        console.log('Component did mount!')
        this.getList();
     }
    getList=()=>{
     /*** method to make api call***/
     fetch('https://gorest.co.in/public/v2/users')
        .then(response => response.json())
        .then(data => this.setState({ list:data }));
    }
     shouldComponentUpdate(nextProps, nextState){
       return this.state.list!==nextState.list
      }
     componentWillUpdate(nextProps, nextState) {
        console.log('Component will update!');
     }
     componentDidUpdate(prevProps, prevState) {
        console.log('Component did update!')
     }
    render() {
        return (
           <div>
              <h3>Mounting Lifecycle Methods</h3>
           </div>
        );
     }
  }