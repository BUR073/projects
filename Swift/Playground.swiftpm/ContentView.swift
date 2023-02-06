import SwiftUI

struct ContentView: View {
    @State private var showDetails = 0

    var body: some View {
        VStack(alignment: .leading) {
            Button("Show details") {
                showDetails = 1
            }
            
            Button("Show details 2") {
                showDetails = 2
            }

            if showDetails == 1 {
                Text("It works")
                    .font(.largeTitle)
            }
            
            if showDetails == 2 {
                Text("It works 2.0")
                
                
                    
            }
        }
        
    }
}
