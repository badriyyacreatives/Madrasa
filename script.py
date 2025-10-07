# Create the complete updated HTML with the correct table layout: Students as rows, Tasks as columns (rotated)

complete_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Madrasa Manager</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <meta name="theme-color" content="#14b8a6">
    <style>
        .hide { display: none !important; }
        .fade-in { animation: fadeIn 0.3s ease-in; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        .slide-up { animation: slideUp 0.3s ease-out; }
        @keyframes slideUp { from { transform: translateY(100%); } to { transform: translateY(0); } }
        
        /* PWA Styles */
        body {
            -webkit-user-select: none;
            -webkit-touch-callout: none;
            -webkit-tap-highlight-color: transparent;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 4px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 2px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
        
        /* Button active states */
        button:active {
            transform: scale(0.98);
        }
        
        /* Modal animations */
        .modal-backdrop {
            backdrop-filter: blur(4px);
        }
        
        /* Loading spinner */
        .spinner {
            border: 2px solid #f3f4f6;
            border-top: 2px solid #14b8a6;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Enhanced button styles */
        .btn-primary {
            background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%);
            transition: all 0.2s ease;
        }
        
        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(20, 184, 166, 0.3);
        }
        
        /* Card hover effects */
        .card-hover:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }
        
        /* Progress bar animation */
        .progress-bar {
            transition: width 0.6s ease-in-out;
        }
        
        /* Status badges */
        .status-present { background-color: #dcfce7; color: #166534; }
        .status-late { background-color: #fed7aa; color: #9a3412; }
        .status-absent { background-color: #fecaca; color: #991b1b; }
        .status-leave { background-color: #dbeafe; color: #1e40af; }
        
        /* Task table styles - Students as rows, Tasks as columns */
        .task-master-table {
            border-collapse: separate;
            border-spacing: 0;
            min-width: 100%;
        }
        
        .task-master-table th {
            background-color: #f8fafc;
            font-weight: 600;
            text-align: center;
            border: 1px solid #e2e8f0;
            font-size: 14px;
            position: relative;
            color: #374151;
        }
        
        .task-master-table td {
            border: 1px solid #e2e8f0;
            text-align: center;
            padding: 12px 8px;
            background-color: white;
            min-width: 60px;
        }
        
        .task-master-table th:first-child,
        .task-master-table td:first-child {
            text-align: left;
            padding-left: 16px;
            font-weight: 500;
            background-color: #f8fafc;
            position: sticky;
            left: 0;
            z-index: 10;
            min-width: 150px;
            color: #111827;
        }
        
        .task-master-table tr:hover td {
            background-color: #f0fdf4;
        }
        
        .task-master-table tr:hover td:first-child {
            background-color: #f0f9ff;
        }
        
        /* Rotated task name headers */
        .rotated-task-header {
            writing-mode: vertical-rl;
            text-orientation: mixed;
            transform: rotate(180deg);
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8px 4px;
            font-size: 13px;
            font-weight: 600;
            line-height: 1.2;
            color: #374151;
            white-space: nowrap;
        }
        
        /* Task header container with delete button */
        .task-header-container {
            position: relative;
            height: 140px;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 8px 4px;
        }
        
        .task-delete-btn {
            position: absolute;
            top: 4px;
            right: 4px;
            z-index: 15;
            background: rgba(239, 68, 68, 0.9);
            color: white;
            border: none;
            border-radius: 4px;
            width: 20px;
            height: 20px;
            font-size: 12px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }
        
        .task-delete-btn:hover {
            background: rgba(185, 28, 28, 1);
            transform: scale(1.1);
        }
        
        /* Checkbox styles for task completion */
        .task-checkbox {
            width: 22px;
            height: 22px;
            border: 2px solid #d1d5db;
            border-radius: 4px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            margin: 0 auto;
        }
        
        .task-checkbox.completed {
            background-color: #10b981;
            border-color: #10b981;
            color: white;
        }
        
        .task-checkbox:hover {
            border-color: #10b981;
            background-color: #ecfdf5;
        }
        
        .task-checkbox.completed:hover {
            background-color: #059669;
        }
        
        /* Scrollable table container */
        .table-container {
            overflow-x: auto;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            max-width: 100%;
        }
        
        /* Mobile optimizations */
        @media (max-width: 640px) {
            .mobile-text { font-size: 14px; }
            .mobile-padding { padding: 12px; }
            
            .task-master-table th,
            .task-master-table td {
                min-width: 50px;
                padding: 8px 4px;
            }
            
            .task-master-table th:first-child,
            .task-master-table td:first-child {
                min-width: 120px;
                padding-left: 12px;
            }
            
            .rotated-task-header {
                height: 100px;
                font-size: 11px;
            }
            
            .task-header-container {
                height: 120px;
            }
            
            .task-checkbox {
                width: 18px;
                height: 18px;
            }
            
            .task-delete-btn {
                width: 18px;
                height: 18px;
                font-size: 10px;
            }
        }
        
        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            :root {
                color-scheme: dark;
            }
        }
    </style>
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiTWFkcmFzYSBNYW5hZ2VyIiwic2hvcnRfbmFtZSI6Ik1hZHJhc2EiLCJkZXNjcmlwdGlvbiI6IkNvbXBsZXRlIGNsYXNzcm9vbSBtYW5hZ2VtZW50IHN5c3RlbSBmb3IgTWFkcmFzYSIsInN0YXJ0X3VybCI6Ii8iLCJkaXNwbGF5Ijoic3RhbmRhbG9uZSIsImJhY2tncm91bmRfY29sb3IiOiIjZmZmZmZmIiwidGhlbWVfY29sb3IiOiIjMTRiOGE2Iiwib3JpZW50YXRpb24iOiJwb3J0cmFpdC1wcmltYXJ5IiwiaWNvbnMiOlt7InNyYyI6ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwaU1UazJJaUJvWldsbmFIUTlJakU1TmtGalpIUnlQU0pwYm1GaVpXeHNSekVnTWpJMklESTFOU0F5TlRVZ01qSTJJaUJXYVdWM1FtOTRQU0k0SURBZ09DQXhPVFlnTVRrMklpQm1hV3hzUFNKdWIyNWxJaUIyWlhKemFXOXVQU0l4TGpFaWJXOTBhVzlOVVhSdmNua3VjbVZ6ZEhKcFkzUktjUT09IiwibWltZVR5cGUiOiJpbWFnZS9zdmcreG1sIiwic2l6ZXMiOiJhbnkifV0sImNhdGVnb3JpZXMiOlsiZWR1Y2F0aW9uIiwicHJvZHVjdGl2aXR5Il0sImxhbmciOiJlbiIsImRpciI6Imx0ciJ9">
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- Landing/Class Selection Page -->
    <div id="landing-page" class="min-h-screen flex flex-col items-center justify-center px-4">
        <div class="bg-teal-500 w-24 h-24 rounded-full flex items-center justify-center mb-8 card-hover transition-all duration-300">
            <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
            </svg>
        </div>
        
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Madrasa Manager</h1>
        <p class="text-gray-600 mb-8 text-center">Select your class to continue</p>
        
        <div id="class-list" class="w-full max-w-md space-y-3 mb-6">
            <!-- Classes will be populated here -->
        </div>
        
        <button id="create-class-btn" class="w-full max-w-md btn-primary text-white py-3 px-4 rounded-lg font-medium flex items-center justify-center gap-2 transition-all">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
            </svg>
            Create New Class
        </button>
    </div>

    <!-- Main App Container -->
    <div id="main-app" class="hide">
        <!-- Header -->
        <header class="bg-teal-500 text-white px-4 py-3 flex items-center justify-between sticky top-0 z-40">
            <div class="flex items-center gap-3">
                <div>
                    <h1 id="page-title" class="text-lg font-medium">Dashboard</h1>
                    <p id="class-name" class="text-teal-100 text-sm"></p>
                </div>
            </div>
            <button id="logout-btn" class="p-2 rounded-lg hover:bg-teal-600 transition-colors">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
                </svg>
            </button>
        </header>

        <!-- Main Content -->
        <main id="main-content" class="pb-20 min-h-screen">
            <!-- Dashboard Page -->
            <div id="dashboard-page" class="page-content p-4">
                <div class="mb-6">
                    <h2 class="text-gray-600 text-sm font-medium mb-4">Today's Overview</h2>
                    
                    <!-- Dashboard Filters will be inserted here dynamically -->
                    
                    <div class="bg-white rounded-lg p-4 mb-4 card-hover transition-all duration-300">
                        <div class="grid grid-cols-2 gap-4 mb-4">
                            <div class="text-sm">
                                <span class="text-gray-600">Period</span>
                                <p id="current-date" class="font-medium"></p>
                            </div>
                            <div class="text-sm">
                                <span class="text-gray-600">Class Time</span>
                                <p id="class-time" class="font-medium"></p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-6">
                        <h3 class="text-gray-600 text-sm font-medium mb-3">Attendance Statistics</h3>
                        <div class="grid grid-cols-2 gap-3">
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-teal-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                                    </svg>
                                </div>
                                <p id="total-students" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Total Students</p>
                            </div>
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-green-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                </div>
                                <p id="present-count" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Present</p>
                            </div>
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-orange-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </div>
                                <p id="late-count" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Late</p>
                            </div>
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-red-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                                    </svg>
                                </div>
                                <p id="absent-count" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Absent</p>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg p-4 card-hover transition-all duration-300">
                        <h3 class="text-gray-600 text-sm font-medium mb-3">Quick Actions</h3>
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="font-medium">Pending Tasks</p>
                                <p class="text-gray-600 text-sm">Tasks to be completed today</p>
                            </div>
                            <div class="bg-red-500 text-white text-sm font-bold rounded-full w-8 h-8 flex items-center justify-center" id="pending-tasks-count">0</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Classes Page -->
            <div id="classes-page" class="page-content hide p-4">
                <div class="flex items-center justify-between mb-4">
                    <h2 class="text-gray-600 text-sm font-medium">Students</h2>
                    <button id="add-student-btn" class="btn-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 text-sm font-medium transition-all">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                        </svg>
                        Add Student
                    </button>
                </div>
                
                <div class="bg-white rounded-lg card-hover transition-all duration-300">
                    <div class="p-4 border-b">
                        <div class="flex items-center justify-between">
                            <h3 id="class-header" class="font-semibold text-lg"></h3>
                            <span id="student-count-badge" class="bg-orange-100 text-orange-800 text-xs font-medium px-2 py-1 rounded-full">0 Students</span>
                        </div>
                        <p id="class-schedule" class="text-gray-600 text-sm mt-1"></p>
                    </div>
                    
                    <div id="students-list" class="divide-y">
                        <!-- Students will be populated here -->
                    </div>
                </div>
            </div>

            <!-- Attendance Page -->
            <div id="attendance-page" class="page-content hide p-4">
                <div class="bg-white rounded-lg p-4 mb-4 card-hover transition-all duration-300">
                    <div class="grid grid-cols-2 gap-4">
                        <div class="text-sm">
                            <span class="text-gray-600">Class Time</span>
                            <p id="attendance-class-time" class="font-medium"></p>
                        </div>
                        <div class="text-sm">
                            <span class="text-gray-600">Grace Period</span>
                            <p class="font-medium">5 minutes</p>
                        </div>
                    </div>
                </div>
                
                <!-- Date navigation will be inserted here -->
                
                <div id="attendance-list" class="space-y-3">
                    <!-- Attendance items will be populated here -->
                </div>
            </div>

            <!-- Tasks Page -->
            <div id="tasks-page" class="page-content hide p-4">
                <div class="flex items-center justify-between mb-4">
                    <h2 class="text-gray-600 text-sm font-medium">Daily Tasks</h2>
                    <button id="create-task-btn" class="btn-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 text-sm font-medium transition-all">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
                        </svg>
                        Create Task
                    </button>
                </div>
                
                <div id="tasks-master-container" class="bg-white rounded-lg card-hover transition-all duration-300">
                    <!-- Single master table will be populated here -->
                </div>
            </div>
        </main>

        <!-- Bottom Navigation -->
        <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-50">
            <div class="flex">
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="dashboard">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m0 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h3a1 1 0 001-1V10"></path>
                    </svg>
                    <span class="text-xs">Home</span>
                </button>
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="classes">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                    </svg>
                    <span class="text-xs">Classes</span>
                </button>
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="attendance">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path>
                    </svg>
                    <span class="text-xs">Attendance</span>
                </button>
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="tasks">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
                    </svg>
                    <span class="text-xs">Tasks</span>
                </button>
            </div>
        </nav>
    </div>

    <!-- Modals -->
    <!-- Create Class Modal -->
    <div id="create-class-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-end justify-center z-50 hide">
        <div class="bg-white w-full max-w-md rounded-t-3xl slide-up">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Create New Class</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded transition-colors">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Class Name</label>
                    <input type="text" id="class-name-input" placeholder="e.g., Grade 5 - Quran" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Start Time</label>
                        <input type="time" id="start-time-input" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">End Time</label>
                        <input type="time" id="end-time-input" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all">
                    </div>
                </div>
                <button id="create-class-submit" class="w-full btn-primary text-white py-3 rounded-lg font-medium transition-all">Create Class</button>
            </div>
        </div>
    </div>

    <!-- Add Student Modal -->
    <div id="add-student-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-end justify-center z-50 hide">
        <div class="bg-white w-full max-w-md rounded-t-3xl slide-up">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Add New Student</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded transition-colors">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Student Name</label>
                    <input type="text" id="student-name-input" placeholder="Enter student name" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Roll Number</label>
                    <input type="number" id="roll-number-input" placeholder="Enter roll number" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all">
                </div>
                <button id="add-student-submit" class="w-full btn-primary text-white py-3 rounded-lg font-medium transition-all">Add Student</button>
            </div>
        </div>
    </div>

    <!-- Create Task Modal -->
    <div id="create-task-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-end justify-center z-50 hide">
        <div class="bg-white w-full max-w-md rounded-t-3xl slide-up">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Create New Task</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded transition-colors">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Task Title</label>
                    <input type="text" id="task-title-input" placeholder="e.g., Memorize Surah Al-Fatiha" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Description (Optional)</label>
                    <textarea id="task-description-input" placeholder="Add task details..." rows="3" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all"></textarea>
                </div>
                <button id="create-task-submit" class="w-full btn-primary text-white py-3 rounded-lg font-medium transition-all">Create Task</button>
            </div>
        </div>
    </div>

    <!-- Manual Time Modal -->
    <div id="manual-time-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-center justify-center z-50 hide">
        <div class="bg-white w-full max-w-md mx-4 rounded-lg">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Mark Attendance</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded transition-colors">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <p id="manual-time-student-name" class="font-medium"></p>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Arrival Time</label>
                    <input type="time" id="manual-time-input" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all">
                </div>
                <div class="flex gap-3">
                    <button id="manual-time-cancel" class="flex-1 bg-gray-200 text-gray-700 py-3 rounded-lg font-medium hover:bg-gray-300 transition-colors">Cancel</button>
                    <button id="manual-time-submit" class="flex-1 btn-primary text-white py-3 rounded-lg font-medium transition-all">Mark Present</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Alert Modal -->
    <div id="alert-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-center justify-center z-50 hide">
        <div class="bg-white w-full max-w-sm mx-4 rounded-lg">
            <div class="p-4 text-center">
                <div id="alert-icon" class="w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                </div>
                <h3 id="alert-title" class="text-lg font-semibold mb-2"></h3>
                <p id="alert-message" class="text-gray-600 mb-4"></p>
                <button id="alert-ok" class="w-full btn-primary text-white py-3 rounded-lg font-medium transition-all">OK</button>
            </div>
        </div>
    </div>

    <script>
// Madrasa Manager PWA - Complete Updated Implementation with Fixed Task Table Layout
class MadrasaManager {
    constructor() {
        this.currentClass = null;
        this.currentPage = 'dashboard';
        this.currentView = 'today';
        this.currentAttendanceDate = new Date().toISOString().split('T')[0];
        this.data = {
            classes: JSON.parse(localStorage.getItem('madrasa_classes')) || [],
            students: JSON.parse(localStorage.getItem('madrasa_students')) || {},
            attendance: JSON.parse(localStorage.getItem('madrasa_attendance')) || {},
            tasks: JSON.parse(localStorage.getItem('madrasa_tasks')) || {}
        };
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadLandingPage();
        this.setupAutoAttendance();
        this.registerServiceWorker();
    }

    setupEventListeners() {
        document.getElementById('create-class-btn').addEventListener('click', () => {
            this.showModal('create-class-modal');
        });

        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', (e) => {
                const page = e.currentTarget.dataset.page;
                this.navigateToPage(page);
            });
        });

        document.querySelectorAll('.modal-close').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.hideModal(e.target.closest('.fixed'));
            });
        });

        document.getElementById('create-class-submit').addEventListener('click', () => {
            this.createClass();
        });

        document.getElementById('add-student-submit').addEventListener('click', () => {
            this.addStudent();
        });

        document.getElementById('create-task-submit').addEventListener('click', () => {
            this.createTask();
        });

        document.getElementById('manual-time-submit').addEventListener('click', () => {
            this.submitManualTime();
        });

        document.getElementById('manual-time-cancel').addEventListener('click', () => {
            this.hideModal(document.getElementById('manual-time-modal'));
        });

        document.getElementById('alert-ok').addEventListener('click', () => {
            this.hideModal(document.getElementById('alert-modal'));
        });

        document.getElementById('add-student-btn').addEventListener('click', () => {
            this.showModal('add-student-modal');
        });

        document.getElementById('create-task-btn').addEventListener('click', () => {
            this.showModal('create-task-modal');
        });

        document.getElementById('logout-btn').addEventListener('click', () => {
            this.logout();
        });

        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('view-filter')) {
                const view = e.target.dataset.view;
                this.setView(view);
            }
            
            if (e.target.classList.contains('date-nav')) {
                const direction = e.target.dataset.direction;
                this.navigateDate(direction);
            }
        });
    }

    saveData() {
        localStorage.setItem('madrasa_classes', JSON.stringify(this.data.classes));
        localStorage.setItem('madrasa_students', JSON.stringify(this.data.students));
        localStorage.setItem('madrasa_attendance', JSON.stringify(this.data.attendance));
        localStorage.setItem('madrasa_tasks', JSON.stringify(this.data.tasks));
    }

    loadLandingPage() {
        const classList = document.getElementById('class-list');
        classList.innerHTML = '';

        if (this.data.classes.length === 0) {
            classList.innerHTML = `
                <div class="text-center py-8">
                    <div class="w-16 h-16 bg-gray-200 rounded-full flex items-center justify-center mx-auto mb-4">
                        <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                        </svg>
                    </div>
                    <p class="text-gray-600 font-medium">No classes created yet</p>
                    <p class="text-gray-500 text-sm mt-1">Create your first class to get started</p>
                </div>
            `;
        } else {
            this.data.classes.forEach(cls => {
                const studentCount = this.data.students[cls.id]?.length || 0;
                const classElement = document.createElement('div');
                classElement.className = 'bg-white rounded-lg p-4 cursor-pointer hover:bg-gray-50 transition-all duration-200 card-hover border border-gray-100';
                classElement.innerHTML = `
                    <div class="flex items-center justify-between">
                        <div class="flex-1">
                            <h3 class="font-semibold text-gray-900 text-lg">${cls.name}</h3>
                            <p class="text-gray-600 text-sm mt-1">${studentCount} students enrolled</p>
                        </div>
                        <div class="text-right ml-4">
                            <div class="text-sm font-medium text-teal-600 bg-teal-50 px-2 py-1 rounded">
                                ${cls.startTime} - ${cls.endTime}
                            </div>
                        </div>
                    </div>
                `;
                classElement.addEventListener('click', () => {
                    this.selectClass(cls);
                });
                classList.appendChild(classElement);
            });
        }

        document.getElementById('landing-page').classList.remove('hide');
        document.getElementById('main-app').classList.add('hide');
    }

    selectClass(classData) {
        this.currentClass = classData;
        document.getElementById('landing-page').classList.add('hide');
        document.getElementById('main-app').classList.remove('hide');
        document.getElementById('class-name').textContent = classData.name;
        this.navigateToPage('dashboard');
    }

    createClass() {
        const name = document.getElementById('class-name-input').value.trim();
        const startTime = document.getElementById('start-time-input').value;
        const endTime = document.getElementById('end-time-input').value;

        if (!name || !startTime || !endTime) {
            this.showAlert('Error', 'Please fill in all fields', 'error');
            return;
        }

        if (startTime >= endTime) {
            this.showAlert('Error', 'End time must be after start time', 'error');
            return;
        }

        const newClass = {
            id: Date.now().toString(),
            name,
            startTime,
            endTime,
            createdAt: new Date().toISOString()
        };

        this.data.classes.push(newClass);
        this.data.students[newClass.id] = [];
        this.data.tasks[newClass.id] = [];
        this.data.attendance[newClass.id] = {};

        this.saveData();
        this.hideModal(document.getElementById('create-class-modal'));
        this.loadLandingPage();
        this.showAlert('Success', 'Class created successfully!', 'success');

        document.getElementById('class-name-input').value = '';
        document.getElementById('start-time-input').value = '';
        document.getElementById('end-time-input').value = '';
    }

    navigateToPage(page) {
        document.querySelectorAll('.nav-item').forEach(item => {
            if (item.dataset.page === page) {
                item.classList.add('text-teal-500');
                item.classList.remove('text-gray-400');
            } else {
                item.classList.remove('text-teal-500');
                item.classList.add('text-gray-400');
            }
        });

        document.querySelectorAll('.page-content').forEach(pageEl => {
            pageEl.classList.add('hide');
        });

        document.getElementById(`${page}-page`).classList.remove('hide');

        const titles = {
            dashboard: 'Dashboard',
            classes: 'Class Management',
            attendance: 'Attendance',
            tasks: 'Tasks'
        };
        document.getElementById('page-title').textContent = titles[page];

        this.currentPage = page;

        switch (page) {
            case 'dashboard':
                this.loadDashboard();
                break;
            case 'classes':
                this.loadClasses();
                break;
            case 'attendance':
                this.loadAttendance();
                break;
            case 'tasks':
                this.loadTasks();
                break;
        }
    }

    loadDashboard() {
        if (!this.currentClass) return;

        const dashboardPage = document.getElementById('dashboard-page');
        if (!dashboardPage.querySelector('.dashboard-filters')) {
            const filtersHTML = `
                <div class="dashboard-filters mb-6">
                    <div class="flex bg-gray-100 rounded-lg p-1 mb-4">
                        <button class="view-filter flex-1 py-2 px-3 rounded-md text-sm font-medium transition-all ${this.currentView === 'today' ? 'bg-white text-teal-600 shadow-sm' : 'text-gray-600 hover:text-teal-600'}" data-view="today">Today</button>
                        <button class="view-filter flex-1 py-2 px-3 rounded-md text-sm font-medium transition-all ${this.currentView === 'week' ? 'bg-white text-teal-600 shadow-sm' : 'text-gray-600 hover:text-teal-600'}" data-view="week">Week</button>
                        <button class="view-filter flex-1 py-2 px-3 rounded-md text-sm font-medium transition-all ${this.currentView === 'month' ? 'bg-white text-teal-600 shadow-sm' : 'text-gray-600 hover:text-teal-600'}" data-view="month">Month</button>
                        <button class="view-filter flex-1 py-2 px-3 rounded-md text-sm font-medium transition-all ${this.currentView === 'year' ? 'bg-white text-teal-600 shadow-sm' : 'text-gray-600 hover:text-teal-600'}" data-view="year">Year</button>
                    </div>
                </div>
            `;
            
            const firstChild = dashboardPage.firstElementChild;
            firstChild.insertAdjacentHTML('afterend', filtersHTML);
        }

        const overviewSection = dashboardPage.querySelector('h2');
        overviewSection.textContent = `${this.getPeriodTitle()} Overview`;

        const periodText = this.getCurrentPeriodText();
        document.getElementById('current-date').textContent = periodText;
        document.getElementById('class-time').textContent = `${this.currentClass.startTime} - ${this.currentClass.endTime}`;

        const stats = this.calculateDashboardStats();
        
        document.getElementById('total-students').textContent = stats.totalStudents;
        document.getElementById('present-count').textContent = stats.present;
        document.getElementById('late-count').textContent = stats.late;
        document.getElementById('absent-count').textContent = stats.absent;

        const tasks = this.data.tasks[this.currentClass.id] || [];
        const students = this.data.students[this.currentClass.id] || [];
        let pendingCount = 0;
        tasks.forEach(task => {
            students.forEach(student => {
                if (!task.completed || !task.completed[student.id]) {
                    pendingCount++;
                }
            });
        });
        document.getElementById('pending-tasks-count').textContent = pendingCount;

        this.addAttendanceTrends();
    }

    addAttendanceTrends() {
        const dashboardPage = document.getElementById('dashboard-page');
        let trendsSection = dashboardPage.querySelector('.trends-section');
        
        if (this.currentView !== 'today' && this.data.students[this.currentClass.id]?.length > 0) {
            if (!trendsSection) {
                trendsSection = document.createElement('div');
                trendsSection.className = 'trends-section mb-6';
                dashboardPage.appendChild(trendsSection);
            }
            
            const trendsData = this.getAttendanceTrends();
            if (trendsData.length > 0) {
                trendsSection.innerHTML = `
                    <div class="bg-white rounded-lg p-4 card-hover transition-all duration-300">
                        <h3 class="text-gray-600 text-sm font-medium mb-4">Attendance Trends</h3>
                        <div class="space-y-3">
                            ${trendsData.map(day => `
                                <div class="flex items-center justify-between py-2">
                                    <span class="text-sm font-medium text-gray-700">${day.label}</span>
                                    <div class="flex items-center gap-3">
                                        <div class="flex items-center gap-1">
                                            <div class="w-3 h-3 bg-green-500 rounded-full"></div>
                                            <span class="text-sm text-gray-600">${day.present}</span>
                                        </div>
                                        <div class="flex items-center gap-1">
                                            <div class="w-3 h-3 bg-orange-500 rounded-full"></div>
                                            <span class="text-sm text-gray-600">${day.late}</span>
                                        </div>
                                        <div class="flex items-center gap-1">
                                            <div class="w-3 h-3 bg-red-500 rounded-full"></div>
                                            <span class="text-sm text-gray-600">${day.absent}</span>
                                        </div>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
            }
        } else if (trendsSection) {
            trendsSection.remove();
        }
    }

    loadAttendance() {
        if (!this.currentClass) return;

        const attendancePage = document.getElementById('attendance-page');
        
        if (!attendancePage.querySelector('.date-navigation')) {
            const dateNavHTML = `
                <div class="date-navigation mb-4">
                    <div class="flex items-center justify-between bg-white rounded-lg p-3 card-hover transition-all duration-300">
                        <button class="date-nav p-2 rounded-lg hover:bg-gray-100 transition-colors" data-direction="prev">
                            <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                            </svg>
                        </button>
                        <div class="text-center">
                            <h3 id="attendance-date-display" class="font-medium text-lg text-gray-900"></h3>
                            <p class="text-gray-600 text-sm" id="attendance-day-name"></p>
                        </div>
                        <button class="date-nav p-2 rounded-lg hover:bg-gray-100 transition-colors" data-direction="next">
                            <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                        </button>
                    </div>
                </div>
            `;
            
            const firstChild = attendancePage.firstElementChild;
            firstChild.insertAdjacentHTML('afterend', dateNavHTML);
        }

        const selectedDate = new Date(this.currentAttendanceDate);
        document.getElementById('attendance-date-display').textContent = selectedDate.toLocaleDateString('en-US', { 
            year: 'numeric', month: 'long', day: 'numeric' 
        });
        document.getElementById('attendance-day-name').textContent = selectedDate.toLocaleDateString('en-US', { weekday: 'long' });

        document.getElementById('attendance-class-time').textContent = `${this.currentClass.startTime} - ${this.currentClass.endTime}`;

        const students = this.data.students[this.currentClass.id] || [];
        const dateAttendance = this.getAttendanceForDate(this.currentAttendanceDate);
        const attendanceList = document.getElementById('attendance-list');
        
        attendanceList.innerHTML = '';

        if (students.length === 0) {
            attendanceList.innerHTML = `
                <div class="bg-white rounded-lg p-6 text-center text-gray-500">
                    <svg class="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                    </svg>
                    <p class="font-medium">No students in this class</p>
                    <p class="text-sm">Add students to start taking attendance</p>
                </div>
            `;
            return;
        }

        const isSelectedFriday = selectedDate.getDay() === 5;
        const isToday = this.currentAttendanceDate === new Date().toISOString().split('T')[0];

        if (isSelectedFriday) {
            attendanceList.innerHTML = `
                <div class="bg-blue-50 rounded-lg p-6 text-center mb-4 card-hover transition-all duration-300">
                    <div class="flex items-center justify-center mb-3">
                        <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center">
                            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                            </svg>
                        </div>
                    </div>
                    <h3 class="font-semibold text-blue-900 mb-2 text-lg">Friday - Weekly Leave</h3>
                    <p class="text-blue-700">All students have automatic leave on Fridays</p>
                </div>
            `;
            return;
        }

        students.forEach(student => {
            const attendance = dateAttendance[student.id];
            
            const studentElement = document.createElement('div');
            studentElement.className = 'bg-white rounded-lg p-4 mb-3 card-hover transition-all duration-300';
            
            this.renderStudentAttendance(studentElement, student, attendance, isToday);
            attendanceList.appendChild(studentElement);
        });
    }

    renderStudentAttendance(element, student, attendance, isToday) {
        let statusBadge = '';
        let timeText = '';
        let actionButtons = '';

        if (attendance) {
            if (attendance.status === 'present') {
                statusBadge = '<span class="status-present text-xs font-medium px-3 py-1 rounded-full">PRESENT</span>';
                timeText = `Marked at ${new Date(attendance.time).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}`;
            } else if (attendance.status === 'late') {
                statusBadge = '<span class="status-late text-xs font-medium px-3 py-1 rounded-full">LATE</span>';
                timeText = `Marked at ${new Date(attendance.time).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}`;
            } else if (attendance.status === 'absent') {
                statusBadge = '<span class="status-absent text-xs font-medium px-3 py-1 rounded-full">ABSENT</span>';
            }
        } else {
            if (isToday) {
                if (this.hasClassTimePassed()) {
                    statusBadge = '<span class="status-absent text-xs font-medium px-3 py-1 rounded-full">ABSENT</span>';
                } else {
                    actionButtons = `
                        <div class="flex gap-2 mt-3">
                            <button onclick="madrasaManager.markPresentNow('${student.id}')" class="btn-primary text-white px-4 py-2 rounded-lg text-sm font-medium flex items-center gap-1 transition-all">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                Present Now
                            </button>
                            <button onclick="madrasaManager.showManualTimeModal('${student.id}', '${student.name}')" class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded-lg text-sm font-medium flex items-center gap-1 transition-all">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                </svg>
                                Set Time
                            </button>
                        </div>
                    `;
                }
            } else {
                actionButtons = `
                    <div class="flex gap-2 mt-3">
                        <button onclick="madrasaManager.markAttendanceForDate('${student.id}', 'present')" class="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded text-xs font-medium transition-colors">Present</button>
                        <button onclick="madrasaManager.markAttendanceForDate('${student.id}', 'late')" class="bg-orange-500 hover:bg-orange-600 text-white px-3 py-1 rounded text-xs font-medium transition-colors">Late</button>
                        <button onclick="madrasaManager.markAttendanceForDate('${student.id}', 'absent')" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-xs font-medium transition-colors">Absent</button>
                    </div>
                `;
            }
        }

        element.innerHTML = `
            <div class="flex items-center justify-between mb-2">
                <div>
                    <h4 class="font-medium text-gray-900">${student.name}</h4>
                    <p class="text-gray-600 text-sm">Roll No: ${student.rollNumber}</p>
                </div>
                ${statusBadge}
            </div>
            ${timeText ? `<div class="flex items-center text-gray-600 text-sm mb-2">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                ${timeText}
            </div>` : ''}
            ${actionButtons}
        `;
    }

    navigateDate(direction) {
        const currentDate = new Date(this.currentAttendanceDate);
        if (direction === 'prev') {
            currentDate.setDate(currentDate.getDate() - 1);
        } else {
            currentDate.setDate(currentDate.getDate() + 1);
        }
        this.currentAttendanceDate = currentDate.toISOString().split('T')[0];
        this.loadAttendance();
    }

    markPresentNow(studentId) {
        const now = new Date();
        this.markAttendanceWithTime(studentId, now, this.currentAttendanceDate);
    }

    showManualTimeModal(studentId, studentName) {
        document.getElementById('manual-time-student-name').textContent = studentName;
        document.getElementById('manual-time-input').value = '';
        document.getElementById('manual-time-modal').dataset.studentId = studentId;
        this.showModal('manual-time-modal');
    }

    submitManualTime() {
        const studentId = document.getElementById('manual-time-modal').dataset.studentId;
        const timeInput = document.getElementById('manual-time-input').value;
        
        if (!timeInput) {
            this.showAlert('Error', 'Please select a time', 'error');
            return;
        }

        const selectedDate = new Date(this.currentAttendanceDate);
        const [hours, minutes] = timeInput.split(':');
        const attendanceTime = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), selectedDate.getDate(), hours, minutes);
        
        this.markAttendanceWithTime(studentId, attendanceTime, this.currentAttendanceDate);
        this.hideModal(document.getElementById('manual-time-modal'));
    }

    markAttendanceForDate(studentId, status) {
        const selectedDate = new Date(this.currentAttendanceDate);
        let time;
        if (status === 'present') {
            time = this.parseTime(this.currentClass.startTime);
        } else if (status === 'late') {
            time = new Date(this.parseTime(this.currentClass.startTime).getTime() + 10 * 60000);
        } else {
            time = new Date();
        }
        
        time = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), selectedDate.getDate(), 
                       time.getHours(), time.getMinutes());
        
        this.storeAttendance(studentId, status, time, this.currentAttendanceDate);
        this.loadAttendance();
        this.showAlert('Success', `Student marked as ${status}`, 'success');
    }

    markAttendanceWithTime(studentId, time, date) {
        if (new Date(date).getDay() === 5) {
            this.showAlert('Info', 'Friday is automatic leave day', 'info');
            return;
        }

        const classStartTime = this.parseTime(this.currentClass.startTime);
        const attendanceDate = new Date(time);
        classStartTime.setFullYear(attendanceDate.getFullYear(), attendanceDate.getMonth(), attendanceDate.getDate());
        
        const timeDiff = time - classStartTime;
        const fiveMinutes = 5 * 60 * 1000;

        const status = timeDiff <= fiveMinutes ? 'present' : 'late';
        
        this.storeAttendance(studentId, status, time, date);
        this.loadAttendance();
        this.showAlert('Success', `Student marked as ${status}`, 'success');
    }

    storeAttendance(studentId, status, time, date) {
        const classId = this.currentClass.id;

        if (!this.data.attendance[classId]) {
            this.data.attendance[classId] = {};
        }
        if (!this.data.attendance[classId][date]) {
            this.data.attendance[classId][date] = {};
        }

        this.data.attendance[classId][date][studentId] = {
            status,
            time: time.toISOString()
        };

        this.saveData();
    }

    getAttendanceForDate(date) {
        const classId = this.currentClass.id;
        return this.data.attendance[classId] && this.data.attendance[classId][date] || {};
    }

    loadClasses() {
        if (!this.currentClass) return;

        const students = this.data.students[this.currentClass.id] || [];
        
        document.getElementById('class-header').textContent = this.currentClass.name;
        document.getElementById('class-schedule').textContent = `Class Time: ${this.currentClass.startTime} - ${this.currentClass.endTime}`;
        document.getElementById('student-count-badge').textContent = `${students.length} Students`;

        const studentsList = document.getElementById('students-list');
        studentsList.innerHTML = '';

        if (students.length === 0) {
            studentsList.innerHTML = `
                <div class="p-6 text-center text-gray-500">
                    <svg class="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                    </svg>
                    <p class="font-medium">No students added yet</p>
                    <p class="text-sm">Click "Add Student" to get started</p>
                </div>
            `;
            return;
        }

        students.forEach(student => {
            const studentElement = document.createElement('div');
            studentElement.className = 'p-4 flex items-center justify-between hover:bg-gray-50 transition-colors';
            studentElement.innerHTML = `
                <div>
                    <h4 class="font-medium text-gray-900">${student.name}</h4>
                    <p class="text-gray-600 text-sm">Roll No: ${student.rollNumber}</p>
                </div>
                <button class="text-red-500 hover:bg-red-50 p-2 rounded transition-colors" onclick="madrasaManager.removeStudent('${student.id}')">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                    </svg>
                </button>
            `;
            studentsList.appendChild(studentElement);
        });
    }

    addStudent() {
        const name = document.getElementById('student-name-input').value.trim();
        const rollNumber = document.getElementById('roll-number-input').value.trim();

        if (!name || !rollNumber) {
            this.showAlert('Error', 'Please fill in all fields', 'error');
            return;
        }

        const students = this.data.students[this.currentClass.id] || [];
        
        if (students.some(s => s.rollNumber === rollNumber)) {
            this.showAlert('Error', 'Roll number already exists', 'error');
            return;
        }

        const newStudent = {
            id: Date.now().toString(),
            name,
            rollNumber,
            createdAt: new Date().toISOString()
        };

        this.data.students[this.currentClass.id].push(newStudent);
        this.saveData();
        
        this.hideModal(document.getElementById('add-student-modal'));
        this.loadClasses();
        this.showAlert('Success', 'Student added successfully!', 'success');

        document.getElementById('student-name-input').value = '';
        document.getElementById('roll-number-input').value = '';
    }

    removeStudent(studentId) {
        if (confirm('Are you sure you want to remove this student?')) {
            this.data.students[this.currentClass.id] = this.data.students[this.currentClass.id].filter(s => s.id !== studentId);
            this.saveData();
            this.loadClasses();
            this.showAlert('Success', 'Student removed successfully!', 'success');
        }
    }

    // Updated Tasks - Students as rows, Tasks as columns (rotated headers)
    loadTasks() {
        if (!this.currentClass) return;

        const tasks = this.data.tasks[this.currentClass.id] || [];
        const students = this.data.students[this.currentClass.id] || [];
        const masterContainer = document.getElementById('tasks-master-container');
        
        masterContainer.innerHTML = '';

        if (students.length === 0) {
            masterContainer.innerHTML = `
                <div class="p-6 text-center text-gray-500">
                    <svg class="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                    </svg>
                    <p class="font-medium">No students in class</p>
                    <p class="text-sm">Add students to assign tasks</p>
                </div>
            `;
            return;
        }

        if (tasks.length === 0) {
            masterContainer.innerHTML = `
                <div class="p-6 text-center text-gray-500">
                    <svg class="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
                    </svg>
                    <p class="font-medium">No tasks created yet</p>
                    <p class="text-sm">Create your first task to get started</p>
                </div>
            `;
            return;
        }

        // Create the single master table - Students as rows, Tasks as columns
        const tableContainer = document.createElement('div');
        tableContainer.className = 'table-container';
        
        const table = document.createElement('table');
        table.className = 'task-master-table';
        
        // Create header row with task names as columns (rotated 90 degrees)
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        
        // First column header (for student names)
        const studentHeaderCell = document.createElement('th');
        studentHeaderCell.textContent = 'Students';
        studentHeaderCell.style.textAlign = 'left';
        headerRow.appendChild(studentHeaderCell);
        
        // Task name columns (rotated)
        tasks.forEach(task => {
            const taskCell = document.createElement('th');
            const headerContainer = document.createElement('div');
            headerContainer.className = 'task-header-container';
            
            // Delete button
            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'task-delete-btn';
            deleteBtn.innerHTML = '×';
            deleteBtn.onclick = () => this.removeTask(task.id);
            headerContainer.appendChild(deleteBtn);
            
            // Rotated task name
            const rotatedDiv = document.createElement('div');
            rotatedDiv.className = 'rotated-task-header';
            rotatedDiv.textContent = task.title;
            headerContainer.appendChild(rotatedDiv);
            
            taskCell.appendChild(headerContainer);
            headerRow.appendChild(taskCell);
        });
        
        thead.appendChild(headerRow);
        table.appendChild(thead);
        
        // Create body with students as rows
        const tbody = document.createElement('tbody');
        
        students.forEach(student => {
            const row = document.createElement('tr');
            
            // Student name cell (first column)
            const studentNameCell = document.createElement('td');
            studentNameCell.innerHTML = `
                <div class="font-medium text-gray-900">${student.name}</div>
                <div class="text-xs text-gray-600 mt-1">Roll: ${student.rollNumber}</div>
            `;
            row.appendChild(studentNameCell);
            
            // Task completion checkboxes for this student
            tasks.forEach(task => {
                const taskCell = document.createElement('td');
                const isCompleted = task.completed && task.completed[student.id];
                
                const checkbox = document.createElement('div');
                checkbox.className = `task-checkbox ${isCompleted ? 'completed' : ''}`;
                checkbox.onclick = () => this.toggleTaskCompletion(task.id, student.id);
                
                if (isCompleted) {
                    checkbox.innerHTML = '<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>';
                }
                
                taskCell.appendChild(checkbox);
                row.appendChild(taskCell);
            });
            
            tbody.appendChild(row);
        });
        
        table.appendChild(tbody);
        tableContainer.appendChild(table);
        masterContainer.appendChild(tableContainer);
    }

    createTask() {
        const title = document.getElementById('task-title-input').value.trim();
        const description = document.getElementById('task-description-input').value.trim();

        if (!title) {
            this.showAlert('Error', 'Please enter a task title', 'error');
            return;
        }

        const newTask = {
            id: Date.now().toString(),
            title,
            description,
            completed: {},
            createdAt: new Date().toISOString()
        };

        if (!this.data.tasks[this.currentClass.id]) {
            this.data.tasks[this.currentClass.id] = [];
        }

        this.data.tasks[this.currentClass.id].push(newTask);
        this.saveData();
        
        this.hideModal(document.getElementById('create-task-modal'));
        this.loadTasks();
        this.showAlert('Success', 'Task created successfully!', 'success');

        document.getElementById('task-title-input').value = '';
        document.getElementById('task-description-input').value = '';
    }

    toggleTaskCompletion(taskId, studentId) {
        const task = this.data.tasks[this.currentClass.id].find(t => t.id === taskId);
        if (!task) return;

        if (!task.completed) {
            task.completed = {};
        }

        task.completed[studentId] = !task.completed[studentId];
        this.saveData();
        this.loadTasks();
    }

    removeTask(taskId) {
        if (confirm('Are you sure you want to remove this task?')) {
            this.data.tasks[this.currentClass.id] = this.data.tasks[this.currentClass.id].filter(t => t.id !== taskId);
            this.saveData();
            this.loadTasks();
            this.showAlert('Success', 'Task removed successfully!', 'success');
        }
    }

    calculateDashboardStats() {
        const students = this.data.students[this.currentClass.id] || [];
        const dates = this.getDatesByView();
        
        let totalPresent = 0, totalLate = 0, totalAbsent = 0;

        dates.forEach(date => {
            const dayOfWeek = new Date(date).getDay();
            if (dayOfWeek === 5) return;
            
            const dateAttendance = this.getAttendanceForDate(date);
            
            students.forEach(student => {
                const attendance = dateAttendance[student.id];
                if (attendance) {
                    if (attendance.status === 'present') totalPresent++;
                    else if (attendance.status === 'late') totalLate++;
                    else if (attendance.status === 'absent') totalAbsent++;
                } else {
                    const dateObj = new Date(date);
                    const today = new Date();
                    if (dateObj < today) {
                        totalAbsent++;
                    }
                }
            });
        });

        return {
            totalStudents: students.length,
            present: totalPresent,
            late: totalLate,
            absent: totalAbsent
        };
    }

    getAttendanceTrends() {
        const dates = this.getDatesByView();
        const students = this.data.students[this.currentClass.id] || [];
        const trends = [];

        dates.forEach(date => {
            const dayOfWeek = new Date(date).getDay();
            if (dayOfWeek === 5) return;
            
            const dateAttendance = this.getAttendanceForDate(date);
            let present = 0, late = 0, absent = 0;
            
            students.forEach(student => {
                const attendance = dateAttendance[student.id];
                if (attendance) {
                    if (attendance.status === 'present') present++;
                    else if (attendance.status === 'late') late++;
                    else if (attendance.status === 'absent') absent++;
                } else {
                    const dateObj = new Date(date);
                    const today = new Date();
                    if (dateObj < today) absent++;
                }
            });

            trends.push({
                label: new Date(date).toLocaleDateString('en-US', { 
                    weekday: 'short', 
                    month: 'short', 
                    day: 'numeric' 
                }),
                present,
                late,
                absent
            });
        });

        return trends.slice(-7);
    }

    setView(view) {
        this.currentView = view;
        
        document.querySelectorAll('.view-filter').forEach(btn => {
            if (btn.dataset.view === view) {
                btn.className = 'view-filter flex-1 py-2 px-3 rounded-md text-sm font-medium transition-all bg-white text-teal-600 shadow-sm';
            } else {
                btn.className = 'view-filter flex-1 py-2 px-3 rounded-md text-sm font-medium transition-all text-gray-600 hover:text-teal-600';
            }
        });
        
        if (this.currentPage === 'dashboard') {
            this.loadDashboard();
        }
    }

    getDatesByView() {
        const today = new Date();
        const dates = [];

        switch (this.currentView) {
            case 'today':
                dates.push(today.toISOString().split('T')[0]);
                break;
            case 'week':
                for (let i = 6; i >= 0; i--) {
                    const date = new Date(today);
                    date.setDate(today.getDate() - i);
                    dates.push(date.toISOString().split('T')[0]);
                }
                break;
            case 'month':
                const startOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
                const endOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0);
                for (let d = new Date(startOfMonth); d <= endOfMonth; d.setDate(d.getDate() + 1)) {
                    dates.push(d.toISOString().split('T')[0]);
                }
                break;
            case 'year':
                const startOfYear = new Date(today.getFullYear(), 0, 1);
                const endOfYear = new Date(today.getFullYear(), 11, 31);
                for (let d = new Date(startOfYear); d <= endOfYear; d.setDate(d.getDate() + 1)) {
                    dates.push(d.toISOString().split('T')[0]);
                }
                break;
        }

        return dates;
    }

    getPeriodTitle() {
        switch (this.currentView) {
            case 'today': return "Today's";
            case 'week': return "This Week's";
            case 'month': return "This Month's";
            case 'year': return "This Year's";
            default: return "Today's";
        }
    }

    getCurrentPeriodText() {
        const today = new Date();
        switch (this.currentView) {
            case 'today':
                return today.toLocaleDateString('en-US', { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' });
            case 'week':
                const weekStart = new Date(today);
                weekStart.setDate(today.getDate() - 6);
                return `${weekStart.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })} - ${today.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}`;
            case 'month':
                return today.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
            case 'year':
                return today.getFullYear().toString();
            default:
                return today.toLocaleDateString('en-US', { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' });
        }
    }

    parseTime(timeString) {
        const today = new Date();
        const [hours, minutes] = timeString.split(':');
        return new Date(today.getFullYear(), today.getMonth(), today.getDate(), hours, minutes);
    }

    hasClassTimePassed() {
        const now = new Date();
        const classEndTime = this.parseTime(this.currentClass.endTime);
        return now > classEndTime;
    }

    getTodayAttendance() {
        const today = new Date().toISOString().split('T')[0];
        return this.getAttendanceForDate(today);
    }

    isFriday() {
        return new Date().getDay() === 5;
    }

    setupAutoAttendance() {
        setInterval(() => {
            if (this.currentClass && this.hasClassTimePassed() && !this.isFriday()) {
                this.markAbsentStudents();
            }
        }, 60000);
    }

    markAbsentStudents() {
        const students = this.data.students[this.currentClass.id] || [];
        const todayAttendance = this.getTodayAttendance();
        const today = new Date().toISOString().split('T')[0];

        let markedAbsent = 0;
        students.forEach(student => {
            if (!todayAttendance[student.id]) {
                this.storeAttendance(student.id, 'absent', new Date(), today);
                markedAbsent++;
            }
        });

        if (markedAbsent > 0) {
            if (this.currentPage === 'attendance') {
                this.loadAttendance();
            }
            if (this.currentPage === 'dashboard') {
                this.loadDashboard();
            }
        }
    }

    showModal(modalId) {
        document.getElementById(modalId).classList.remove('hide');
        document.body.style.overflow = 'hidden';
    }

    hideModal(modal) {
        if (typeof modal === 'string') {
            modal = document.getElementById(modal);
        }
        modal.classList.add('hide');
        document.body.style.overflow = 'auto';
    }

    showAlert(title, message, type = 'success') {
        const alertModal = document.getElementById('alert-modal');
        const alertIcon = document.getElementById('alert-icon');
        const alertTitle = document.getElementById('alert-title');
        const alertMessage = document.getElementById('alert-message');

        alertTitle.textContent = title;
        alertMessage.textContent = message;

        if (type === 'success') {
            alertIcon.className = 'w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center bg-green-100';
            alertIcon.innerHTML = '<svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>';
        } else if (type === 'error') {
            alertIcon.className = 'w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center bg-red-100';
            alertIcon.innerHTML = '<svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>';
        } else if (type === 'info') {
            alertIcon.className = 'w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center bg-blue-100';
            alertIcon.innerHTML = '<svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>';
        }

        this.showModal('alert-modal');
        
        setTimeout(() => {
            this.hideModal(alertModal);
        }, 3000);
    }

    logout() {
        if (confirm('Are you sure you want to logout?')) {
            this.currentClass = null;
            this.currentView = 'today';
            this.loadLandingPage();
        }
    }

    registerServiceWorker() {
        if ('serviceWorker' in navigator) {
            const swCode = `
                const CACHE_NAME = 'madrasa-manager-v1';
                const urlsToCache = [
                    '/',
                    'https://cdn.tailwindcss.com'
                ];

                self.addEventListener('install', event => {
                    event.waitUntil(
                        caches.open(CACHE_NAME)
                            .then(cache => cache.addAll(urlsToCache))
                    );
                });

                self.addEventListener('fetch', event => {
                    event.respondWith(
                        caches.match(event.request)
                            .then(response => response || fetch(event.request))
                    );
                });
            `;
            
            const blob = new Blob([swCode], { type: 'application/javascript' });
            const swURL = URL.createObjectURL(blob);
            
            navigator.serviceWorker.register(swURL)
                .then(registration => {
                    console.log('SW registered successfully');
                })
                .catch(error => {
                    console.log('SW registration failed');
                });
        }
    }
}

// Initialize the application
const madrasaManager = new MadrasaManager();
    </script>
</body>
</html>'''

# Write the complete updated HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(complete_html)

print("✅ Complete updated index.html with corrected task table layout!")
print("📋 FIXED TASK TABLE STRUCTURE:")
print("   • Rows: Student names (with roll numbers)")
print("   • Columns: Task names (rotated 90 degrees vertically)")
print("   • Checkboxes at intersections for completion tracking")
print("   • Fixed color issues for task names in headers")
print("   • Delete buttons positioned at top of each task column")
print("   • Proper text color contrast (#374151) for readability")
print("   • Mobile-optimized responsive design")
print("   • Horizontal scrolling for many tasks")
print("   • Sticky first column for student names")
print("\n🎯 Table Structure:")
print("   Rows: [Ahmad] [Sara] [Ali] [Fatima] ...")
print("   Columns: [Students] [Task 1↻] [Task 2↻] [Task 3↻] ...")
print("   ↻ = Rotated 90 degrees vertically")