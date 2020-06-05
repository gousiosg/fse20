// RUN: llvm-mc -triple i386-unknown-unknown --show-encoding %s | FileCheck %s

// CHECK: invpcid 3809469200(%edx,%eax,4), %eax 
// CHECK: encoding: [0x66,0x0f,0x38,0x82,0x84,0x82,0x10,0xe3,0x0f,0xe3]        
invpcid 3809469200(%edx,%eax,4), %eax 

// CHECK: invpcid 485498096, %eax 
// CHECK: encoding: [0x66,0x0f,0x38,0x82,0x05,0xf0,0x1c,0xf0,0x1c]        
invpcid 485498096, %eax 

// CHECK: invpcid 485498096(%edx,%eax,4), %eax 
// CHECK: encoding: [0x66,0x0f,0x38,0x82,0x84,0x82,0xf0,0x1c,0xf0,0x1c]        
invpcid 485498096(%edx,%eax,4), %eax 

// CHECK: invpcid 485498096(%edx), %eax 
// CHECK: encoding: [0x66,0x0f,0x38,0x82,0x82,0xf0,0x1c,0xf0,0x1c]        
invpcid 485498096(%edx), %eax 

// CHECK: invpcid 64(%edx,%eax), %eax 
// CHECK: encoding: [0x66,0x0f,0x38,0x82,0x44,0x02,0x40]        
invpcid 64(%edx,%eax), %eax 

// CHECK: invpcid (%edx), %eax 
// CHECK: encoding: [0x66,0x0f,0x38,0x82,0x02]        
invpcid (%edx), %eax 

